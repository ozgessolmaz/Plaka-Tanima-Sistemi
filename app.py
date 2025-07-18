from flask import Flask, request, render_template, url_for
from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np
import io
import os
import uuid

app = Flask(__name__)

# Klasörleri oluştur
os.makedirs('static/uploads', exist_ok=True)
os.makedirs('static/results', exist_ok=True)

# Eğittiğin best.pt model dosyasının tam yolunu ver
model = YOLO('runs/detect/train4/weights/best.pt')

COUNTER_FILE = 'counter.txt'

def get_total_detections():
    try:
        with open(COUNTER_FILE, 'r') as f:
            return int(f.read().strip())
    except:
        return 0

def increment_total_detections(count):
    total = get_total_detections() + count
    with open(COUNTER_FILE, 'w') as f:
        f.write(str(total))
    return total

@app.route("/", methods=["GET"])
def index():
    total_detections = get_total_detections()
    return render_template("index.html", total_detections=total_detections)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        file = request.files.get("image")
        if file is None or file.filename == '':
            return render_template("index.html", error="Lütfen bir dosya seçin!", total_detections=get_total_detections())

        unique_id = str(uuid.uuid4())
        original_filename = f"{unique_id}_original.jpg"
        result_filename = f"{unique_id}_result.jpg"

        # Görseli kaydet
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image.save(f"static/uploads/{original_filename}")

        # Model ile tahmin
        results = model(f"static/uploads/{original_filename}")

        boxes = []
        if results[0].boxes is not None and len(results[0].boxes) > 0:
            boxes = results[0].boxes.xyxy.cpu().numpy()

        detection_count = len(boxes)

        # Kutuları çiz
        img = cv2.imread(f"static/uploads/{original_filename}")
        for box in boxes:
            x1, y1, x2, y2 = map(int, box[:4])
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
        cv2.imwrite(f"static/results/{result_filename}", img)

        # Sayaç güncelle
        increment_total_detections(detection_count)

        return render_template("result.html",
                               original_image=f"uploads/{original_filename}",
                               result_image=f"results/{result_filename}",
                               detections=detection_count,
                               total_detections=get_total_detections())

    except Exception as e:
        return render_template("index.html", error=f"Hata oluştu: {str(e)}", total_detections=get_total_detections())

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

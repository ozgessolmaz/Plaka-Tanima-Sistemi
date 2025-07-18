Plaka Tanıma Sistemi


🔍 Proje Tanıtımı
Bu proje, YOLOv8 (You Only Look Once) nesne tespiti algoritması ile eğitilmiş bir modelin, araç plakalarını gerçek zamanlı olarak tespit etmesini ve tanımasını sağlayan bir sistemdir. Sistem, kullanıcı dostu bir web arayüzü ile desteklenmiş, kullanıcıların kolaylıkla fotoğraf veya video yükleyerek plaka tanımlaması yapabileceği bir platform sunar.
Plaka tanıma sistemleri; güvenlik, trafik izleme, otopark yönetimi ve çeşitli kamu/özel sektör uygulamalarında yaygın olarak kullanılmaktadır. Bu projeyle, bu teknolojinin temel prensiplerini uygulamalı olarak öğrenmek ve göstermek hedeflenmiştir.


 
🧠 Kullanılan Teknolojiler ve Kütüphaneler
•	YOLOv8 – Ultralytics tarafından geliştirilen, güncel ve yüksek performanslı nesne tanıma algoritması.
•	Python 3.11+
•	OpenCV – Görüntü işleme işlemleri için.
•	Flask – Arka uç web sunucusu için.
•	HTML/CSS/JS – Basit ve kullanıcı dostu arayüz geliştirme.
•	Torch – Derin öğrenme modellerini çalıştırmak için.
•	Ultralytics API – YOLOv8 entegrasyonu için.


 
🏗️ Projenin Yapısı
bash
KopyalaDüzenle
plate-web-ui/
│
├── static/               # Stil dosyaları, görseller
├── templates/            # HTML şablonları
├── runs/                 # YOLOv8 eğitim çıktı klasörleri
│   └── detect/
│       └── trainX/
│           └── weights/  # Eğitim sonrası .pt dosyaları (best.pt, last.pt)
│
├── app.py                # Flask uygulaması (backend)
├── detect.py             # YOLO model entegrasyonu
├── README.md             # Bu döküman


 
⚙️ YOLOv8 Nedir?
YOLOv8, "You Only Look Once" ailesinin en güncel sürümüdür. Hızlı ve doğru nesne tanıma sağlayan bir algoritmadır. YOLOv8’in başlıca avantajları:
•	Gerçek zamanlı işlemeye uygunluğu
•	Yüksek doğruluk oranları
•	Transfer öğrenmeye uygun yapısı
•	Optimize edilmiş ve küçük model boyutları
Bu proje özelinde, transfer learning kullanılarak var olan bir YOLOv8 modeli eğitilmiş ve plaka verileriyle özelleştirilmiştir.

 
🎯 Projenin Amacı
Bu çalışmanın amacı:
•	YOLOv8 mimarisi ve transfer öğrenme uygulamalarını anlamak
•	Plaka tanıma gibi gerçek dünya problemlerine çözüm üretmek
•	Görüntü işleme + derin öğrenme + web geliştirme disiplinlerini birleştirmek

 
📝 Notlar
•	Arayüz basit tutularak kullanıcı deneyimi ön planda tutulmuştur.
•	YOLOv8 ile yapılan eğitim sonucu ortalama %98 doğruluk elde edilmiştir.


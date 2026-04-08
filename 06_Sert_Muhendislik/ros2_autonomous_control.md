# 🤖 ROS2 ve Otonom Kontrol Mimari Standartları

Otonom makineler için ROS2 (Robot Operating System 2), sistemin sinir sistemi işlevini görür. Bu doküman, hata toleranslı ve yüksek performanslı robotik kontrol için mimari kuralları tanımlar.

---

## 🏗️ Mimari Prensipler

### 1. Mikroservis ve Node Yapısı
- **Yüksek Kohezyon:** Her node tek bir fiziksel veya mantıksal görevi (Örn: Lidar_Driver, Path_Planner) yerine getirmelidir.
- **Asenkron İletişim:** Node'lar arasındaki iletişim `DDS` (Data Distribution Service) üzerinden asenkron şekilde yönetilmelidir.

### 2. QoS (Quality of Service) Ayarları
- **Sensör Verileri:** Best-effort (Düşük gecikme kritik, veri kaybı tolere edilebilir).
- **Komut Verileri:** Reliable (Veri kaybı imkansız olmalıdır; bir roketin veya robotun "dur" komutunu kaçırma lüksü yoktur).

---

## 🛠 Kontrol Döngüleri

### Sensör Füzyonu
- **EKF / SLAM:** Lidar, IMU ve Odometri verilerinin İlk Prensipler bazında (fiziksel olasılıklar) birleştirilmesi.
- **Düşük Gecikmeli İşleme:** Sensör verisi ile komut çıktısı arasındaki döngü süresi (cycle time) < 20ms olmalıdır.

### Güvenlik Katmanı (Emergency Stop)
- Yazılım katmanından bağımsız, fiziksel bir "Watchdog" mekanizması her zaman aktif olmalıdır.

---

## 📊 Ölçütler
- **Jitter:** Node'lar arası iletişimdeki gecikme dalgalanması.
- **CPU Overload:** Maksimum node yükünün çekirdek kapasitesini aşmaması.
- **Bandwidth Usage:** Veri yolundaki doluluk oranı.

---
**Durum:** `Robotik Kontrol Standartları Aktif`

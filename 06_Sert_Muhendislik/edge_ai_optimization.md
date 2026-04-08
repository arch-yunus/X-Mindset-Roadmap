# 🤖 Edge-AI İnferans Optimizasyonu (Optimization)

Otonom bir makine, buluta bağımlı olamaz. Bu doküman, kısıtlı donanımlarda (NVIDIA Jetson, Coral, FPGA) yüksek performanslı AI inferansı için gereken teknikleri kapsar.

---

## 🔬 Optimizasyon Katmanları

### 1. Model Sadeleştirme (Step 2: Deletion)
- **Budama (Pruning):** Ağdaki önemsiz bağlantıları (weights) silerek kütleyi ($m_0$) azaltın. 
- **Bilgi Damıtma (Knowledge Distillation):** Büyük bir öğretici modelden, daha küçük ve hızlı bir öğrenci model türetin.

### 2. Nicemleme (Quantization)
- **FP32'den INT8'e:** 32-bit kayan nokta sayılardan 8-bit tam sayılara geçiş yaparak işlem hızını artırın ve enerji tüketimini Landauer Sınırı'na yaklaştırın.
- **PTQ vs QAT:** Post-Training Quantization (Hızlı) / Quantization-Aware Training (Daha Doğru).

### 3. Donanım Hızlandırma
- **TensorRT:** NVIDIA donanımlarında katman seviyesinde füzyon (layer fusion) ve kernel tuning.
- **Thread Paralelliği:** İşlemci çekirdeklerini %100 yükte ve asenkron şekilde yönetin.

---

## 📊 Performans Metrikleri
- **İnferans Gecikmesi (Latency):** < 10ms (Gerçek zamanlı tepki için).
- **Watt Başına Kare (FPS/W):** Enerji verimliliği.
- **Bellek Ayak İzi:** < 500MB (Gömülü sistemler için).

---
**Durum:** `AI Optimizasyon Çerçevesi Hazır`

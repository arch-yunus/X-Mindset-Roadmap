# 💻 C++ Mühendislik Standartları (High-Stakes Systems)

X-Mindset mühendisliği için kod, sadece çalışan bir sistem değil, hataya yer bırakmayan bir makinedir. Bu doküman, kritik sistemler için C++ uygulama standartlarını tanımlar.

---

## 🛡️ Temel İlkeler

### 1. Bellek Güvenliği (Memory Safety)
- **Raw Pointers Yasaktır:** Sadece `std::unique_ptr` ve `std::shared_ptr` kullanın.
- **RAII:** Kaynak yönetimi her zaman nesne ömür döngüsü ile bağlı olmalıdır.
- **Stack over Heap:** Mümkün olan her yerde veriyi stack üzerinde tutarak bellek parçalanmasını (fragmentation) ve gecikmeyi önleyin.

### 2. Belirlenimcilik (Determinism)
- **Gerçek Zamanlı (Real-time) Kısıtlamalar:** Otonom sistemlerde non-deterministic davranışlar kabul edilemez.
- **Dinamik Bellek Tahsisi:** Çalışma zamanında (runtime) `new` / `malloc` kullanımını minimize edin. Mümkünse memory pooling tekniklerini uygulayın.

---

## 🛠 Teknik Pratikler

```cpp
// KÖTÜ ÖRNEK (Analoji Yoluyla Yazılım)
Object* obj = new Object(); // Silinmesi unutulabilir, leak riski.

// İYİ ÖRNEK (X-Mindset Standardı)
auto obj = std::make_unique<Object>(); // RAII garantili.
```

### Kod İnceleme Kriterleri
- [ ] Gereksiz kütüphane bağımlılıkları ($m_0$) temizlendi mi?
- [ ] Döngü süreleri (cycle time) ölçüldü mü?
- [ ] Hata yakalama mekanizmaları fiziksel güvenliği sağlıyor mu?

---
**Durum:** `Kod Standartları Belirlendi`

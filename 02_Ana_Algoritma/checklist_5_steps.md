# 🛠 Ana Algoritma: 5 Adımlı Mühendislik Kontrol Listesi

Bu kontrol listesi, herhangi bir üretim veya tasarım süreci için mutlak ve değiştirilemez bir protokoldür. **Adımları atlamayın.**

---

## ✅ Adım 1: Gereksinimleri Daha Az Aptalca Yap
- [ ] Bu gereksinimin bir "insan" sahibi var mı? (Departman ismi kabul edilmez).
- [ ] Gereksinimin fiziksel bir temeli var mı yoksa sadece "birisi öyle istediği için" mi orada?
- [ ] Gereksinim, İlk Prensipler süzgecinden geçti mi?

## ✅ Adım 2: Parçayı veya Süreci SİLMEYE ÇALIŞ
- [ ] Bu parça/süreç olmadan sistem çalışır mı?
- [ ] Eğer bu adımı silmezsem, sistemin toplam kütlesi ($m_0$) ne kadar artıyor?
- [ ] *Kural:* Sistem ara sıra bozulmuyorsa, yeterince silmiyorsunuzdur. %10 hata payını hedefleyin.

## ✅ Adım 3: Basitleştir veya Optimize Et
- [ ] Bu parça/süreç 2. Adım'dan sağ çıktı mı? (Sadece hayatta kalanları optimize edin).
- [ ] Tasarım, karmaşıklığı azaltacak şekilde en basit formuna indirgendi mi?
- [ ] Gereksiz ara katmanlar (abstractions) temizlendi mi?

## ✅ Adım 4: Döngü Süresini Hızlandır
- [ ] İlk 3 adım tamamlandı mı? (Bozuk bir sistemi hızlandırmayın).
- [ ] Darboğaz (bottleneck) neresi?
- [ ] Hızı 2 katına çıkaracak radikal bir değişiklik yapılabilir mi?

## ✅ Adım 5: Otomatize Et
- [ ] Süreç matematiksel olarak rafine edildi mi?
- [ ] Manuel olarak mükemmel işliyor mu? (Bir karmaşayı asla otomatize etmeyin).
- [ ] Robotlar veya scriptler son dokunuş olarak eklendi mi?

---
**Mutlak Kural:** Optimizasyon (Adım 3), Silme (Adım 2) işleminden sonra gelmelidir.
**Durum:** `Algoritma Uygulama Hazır`

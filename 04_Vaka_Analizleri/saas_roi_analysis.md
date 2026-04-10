# 📊 Vaka Analizi: SaaS ve Yazılım Kütlesinin (m0) İlk Prensipler Analizi

> **Aksiyom:** Bir yazılımın değeri, çözdüğü problemin ölçeği ile doğru, bakımını yapmak için gereken "bilişsel yük" (entropy) ile ters orantılıdır.

Modern işletmelerde SaaS (Software as a Service) abonelikleri, genellikle "analoji yoluyla" (herkes kullanıyor, o halde biz de kullanmalıyız) satın alınır. Bu vaka, bu dogmayı İlk Prensipler ile yıkar.

---

## 1. Analoji Yoluyla Karar Verme (Status Quo)
- "Satış ekibimiz için Salesforce'a ihtiyacımız var çünkü endüstri standardı bu."
- "Slack kullanmalıyız çünkü hızlı iletişim sağlıyor."
- Arka planda: 100+ farklı abonelik, her biri için ayrı kimlik yönetimi, veri siloları ve yıllık milyon dolarlık maliyet.

## 2. İlk Prensipler Yapısökümü (Deconstruction)
- **Problem Nedir?** Müşteri verilerini saklamak, satış süreçlerini takip etmek ve ekipler arası bilgi akışını sağlamak.
- **Mutlak Gereksinimler:**
    1. Veri tabanı (yapılandırılmış veri).
    2. Arayüz (veriyi okumak/yazmak).
    3. Haberleşme katmanı.
- **Maliyet Analizi (Sihirli Değnek Metodu):** 
    - AWS/Azure gibi bir bulut sağlayıcısında ham veri depolama ve hesaplama maliyeti, Salesforce abonelik ücretinin yaklaşık %1'idir.
    - Aradaki %99, pazarlama, satış ekipleri ve Salesforce'un genel giderleridir.

## 3. Sıfırdan Yeniden İnşa Et (The Reconstruction)
Eğer bir mühendislik takımıysanız, 3. taraf devasa SaaS paketleri satın almak yerine:
- **Vertical Integration:** Kendi hafif (lightweight) dahili araçlarınızı inşa edin. 
- **Step 2 Uygulaması (Sil):** Gereksiz özellikleri (SaaS'ın size zorla sunduğu %80'lik kısım) tamamen atın.
- **Sonuç:** Bilişsel kütle ($m_0$) düşer, veri egemenliği artar ve maliyet tabanı üstel olarak azalır.

---

## 💡 X-Mindset Çıkarımı
"Bedava" veya "Hazır" çözümler, sistem mimarinize eklenen gizli kütlelerdir. Her dış bağımlılık, Tsiolkovsky Roket Denklemi'ndeki $m_0$ kütlesini artırarak projenizin nihai hızını ($\Delta v$) düşürür.

> **"Kendi araçlarını inşa eden, kendi kaderini de inşa eder."**

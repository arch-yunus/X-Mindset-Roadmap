name: "🚀 İlk Prensipler Önerisi (First Principles Proposal)"
description: "Sisteme yeni bir gereksinim veya özellik eklemek için axiomatization temelli teklif."
title: "[PROPOSAL] - <Özet Başlık>"
labels: ["enhancement", "first-principles"]
body:
  - type: markdown
    attributes:
      value: |
        **X-Mindset Meta-Engineering Research Lab'e hoş geldiniz.**
        Herhangi bir ekleme yapmadan önce, bu değişikliğin neden "kaçınılmaz" olduğunu kanıtlamanız gerekir.
  - type: input
    id: dogma
    attributes:
      label: "1. Mevcut Dogma / Analoji"
      description: "Bu sorun şu anda endüstride veya diğer projelerde genellikle nasıl 'yanlış' veya 'hantal' bir şekilde çözülüyor?"
      placeholder: "Örn: Herkes X kütüphanesini kullanıyor çünkü standart bu..."
    validations:
      required: true
  - type: textarea
    id: axioms
    attributes:
      label: "2. Yapısöküm / Aksiyomlar"
      description: "Sorunu mutlak fiziksel veya mantıksal gerçeklerine ayırın."
    validations:
      required: true
  - type: textarea
    id: reconstruction
    attributes:
      label: "3. Önerilen Çözüm (Yeniden İnşa)"
      description: "Aksiyomlar üzerine inşa edilmiş, en basit ve en hızlı çözüm nedir?"
    validations:
      required: true
  - type: checkboxes
    id: algorithm-check
    attributes:
      label: "Algoritma Uyumluluğu"
      options:
        - label: "Adım 1: Gereksinimleri sorguladım."
          required: true
        - label: "Adım 2: Silinebilecek her şeyi sildiğimden eminim."
          required: true
        - label: "Adım 3: Bu çözümün en basit form olduğuna inanıyorum."
          required: true

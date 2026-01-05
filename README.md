# Rastgele Sayı Üreteci (RSA + AES-CTR)

Bu proje, kriptografik olarak güvenli bir rastgele sayı üreteci (CSPRNG) uygulamasıdır. Hibrit bir yaklaşım kullanarak hem RSA'nın matematiksel karmaşıklığını hem de AES'in hızını ve güvenliğini birleştirir.

## 🚀 Proje Yapısı

```text
rastgele-sayi-ureteci/
│
├── main.py             # Ana üreteç motoru (RSA + AES-CTR)
├── analysis.py         # İstatistiksel analiz ve entropi hesaplama
│
├── README.md           # Proje dökümantasyonu
│
├── outputs/            # Üretilen veriler ve raporlar
│   ├── random_bits.txt      # Üretilen ham rastgele bitler
│   ├── bit_statistics.txt   # Frekans ve entropi analiz sonuçları
│   └── seed_tests.txt       # Başlangıç değeri (seed) doğrulama testleri
│
└── docs/               # Görsel dökümantasyon
    └── flowchart.png   # Sistemin çalışma mantığı (Flowchart)
```

## 🛠️ Çalışma Mantığı

Sistem üç temel aşamadan oluşur:

1. **Güvenli Seed Üretimi (RSA):** OS tabanlı rastgele bir değer, 2048-bit RSA anahtarı ile şifrelenerek yüksek entropili bir başlangıç değeri (seed) oluşturulur.
2. **Key Derivation (SHA-256):** Oluşturulan seed, SHA-256 karma fonksiyonundan geçirilerek AES-256 için güvenli bir anahtar türetilir.
3. **Rastgele Veri Üretimi (AES-CTR):** Türetilen anahtar kullanılarak AES algoritması Counter (Sayaç) modunda çalıştırılır ve sonsuz bir rastgele veri akışı sağlanır.

## � Matematiksel Temel

### 1. RSA Seed Üretimi
$$ S = x^e \pmod{n} $$
Burada:
- $x$: İşletim sisteminden alınan 32-byte'lık rastgele başlangıç vektörü.
- $e$: RSA açık anahtar üssü (65537).
- $n$: RSA modülü (2048-bit).
- $S$: Üretilen yüksek entropili seed.

### 2. AES-CTR Üretim Denklemi
$$ R_i = E_K(i) $$
Burada:
- $K = \text{SHA256}(S)$: Türetilen 256-bit AES anahtarı.
- $i$: 128-bit sayaç değeri.
- $E_K$: $K$ anahtarı ile AES şifreleme fonksiyonu.
- $R_i$: Üretilen $i$. rastgele veri bloğu.

## 📝 Sözde Kod (Pseudocode)

```text
ALGORİTMA RSA_AES_CTR_RNG:
    GİRDİ: RSA_Açık_Anahtar(n, e), Sayaç i = 0
    ÇIKTI: Rastgele Bayt Akışı

    1. x = OS_Rastgele_Bayt(32)
    2. Seed S = (x^e) mod n
    3. Anahtar K = SHA256(S)
    
    DÖNGÜ (Her blok talebi için):
        a. Blok = AES_Şifrele(K, i)
        b. i = i + 1
        c. Blok'u döndür
    DÖNGÜ SONU
```

## �📊 Analiz ve Doğrulama

`analysis.py` modülü, üretilen veriler üzerinde şu testleri gerçekleştirir:
- **Bit Frekans Testi:** 0 ve 1 bitlerinin dağılım başarımı.
- **Shannon Entropisi:** Verinin tahmin edilemezlik derecesi (İdeal değer: 8.0 bit/byte).

## 💻 Kullanım

1. **Gereksinimler:**
   ```bash
   pip install pycryptodome
   ```

2. **Üretimi Başlat:**
   ```bash
   python main.py
   ```

3. **Analiz Yap:**
   ```bash
   python analysis.py
   ```

---
*Bu proje eğitim amaçlı geliştirilmiş bir kriptografik uygulama örneğidir.*

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os

# ---------- 1. RSA ile Güvenli Seed Üretimi ----------
# 2048-bit RSA anahtarı oluşturuluyor
rsa_key = RSA.generate(2048)
n = rsa_key.n
e = rsa_key.e

# Rastgele başlangıç değeri (OS urandom'dan)
x = int.from_bytes(os.urandom(32), 'big')

# RSA işlemi (seed) - Bu adım matematiksel karmaşıklığı artırır
seed = pow(x, e, n).to_bytes(256, 'big')

# ---------- 2. AES Anahtar Türetme ----------
# Seed değerinden SHA-256 ile 256-bit AES anahtarı türetiliyor
aes_key = SHA256.new(seed).digest()

# ---------- 3. AES-CTR Rastgele Sayı Üreteci ----------
counter = 0

def secure_random():
    global counter
    # Her çağrıda yeni bir AES nesnesi oluşturulur (ECB modunda sayaç şifreleme CTR etkisi yaratır)
    cipher = AES.new(aes_key, AES.MODE_ECB)
    counter_bytes = counter.to_bytes(16, 'big')
    counter += 1
    return cipher.encrypt(counter_bytes)

# ---------- Test ve Dosya Yazma ----------
if __name__ == "__main__":
    print("RSA+AES-CTR Rastgele Sayı Üreteci Başlatıldı.")
    print("Seed oluşturuldu ve anahtar türetildi.")
    
    output_path = os.path.join("outputs", "random_bits.txt")
    
    # 1 MB'lık rastgele veri üret ve kaydet (Analiz için)
    target_size = 1024 * 1024  # 1 MB
    generated_size = 0
    
    print(f"Veriler '{output_path}' dosyasına yazılıyor...")
    
    with open(output_path, "wb") as f:
        while generated_size < target_size:
            random_block = secure_random()
            f.write(random_block)
            generated_size += len(random_block)
            
    print(f"Tamamlandı! Toplam {generated_size} bayt rastgele veri üretildi.")
    
    # Ekrana örnek gösterim
    print("\nÖrnek Çıktılar (Hex formatında):")
    print("Random 1:", secure_random().hex())
    print("Random 2:", secure_random().hex())
    print("Random 3:", secure_random().hex())

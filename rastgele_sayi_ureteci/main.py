from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os

# ---------- 1. RSA ile Güvenli Seed Üretimi ----------
rsa_key = RSA.generate(2048)
n = rsa_key.n
e = rsa_key.e

# Rastgele başlangıç değeri
x = int.from_bytes(os.urandom(32), 'big')

# RSA işlemi (seed)
seed = pow(x, e, n).to_bytes(256, 'big')

# ---------- 2. AES Anahtar Türetme ----------
aes_key = SHA256.new(seed).digest()  # 256-bit AES key

# ---------- 3. AES-CTR Rastgele Sayı Üreteci ----------
counter = 0

def secure_random():
    global counter
    cipher = AES.new(aes_key, AES.MODE_ECB)
    counter_bytes = counter.to_bytes(16, 'big')
    counter += 1
    return cipher.encrypt(counter_bytes)

# ---------- Test ----------
print("Random 1:", secure_random().hex())
print("Random 2:", secure_random().hex())
print("Random 3:", secure_random().hex())

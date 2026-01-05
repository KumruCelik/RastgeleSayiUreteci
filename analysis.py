import os
import math
from collections import Counter

def analiz_et(dosya_yolu):
    if not os.path.exists(dosya_yolu):
        print(f"Hata: {dosya_yolu} bulunamadı. Lütfen önce main.py'yi çalıştırın.")
        return

    print(f"Analiz ediliyor: {dosya_yolu}")
    
    # Dosyayı oku
    with open(dosya_yolu, 'rb') as f:
        data = f.read()
    
    total_bytes = len(data)
    total_bits = total_bytes * 8
    
    # 1. Bit Sayımı (0 ve 1 frekansı)
    bit_string = ''.join(f'{byte:08b}' for byte in data)
    counts = Counter(bit_string)
    
    zeros = counts['0']
    ones = counts['1']
    
    # 2. Entropi Hesaplama (Shannon Entropy - byte tabanlı)
    byte_counts = Counter(data)
    entropy = 0
    for count in byte_counts.values():
        p_x = count / total_bytes
        entropy += -p_x * math.log2(p_x)
    
    # Sonuçları hazırla
    sonuclar = []
    sonuclar.append("-" * 30)
    sonuclar.append("İSTATİSTİKSEL ANALİZ SONUÇLARI")
    sonuclar.append("-" * 30)
    sonuclar.append(f"Toplam Veri        : {total_bytes} byte ({total_bits} bit)")
    sonuclar.append(f"0 Sayısı           : {zeros} (%{zeros/total_bits*100:.4f})")
    sonuclar.append(f"1 Sayısı           : {ones} (%{ones/total_bits*100:.4f})")
    sonuclar.append(f"Fark               : {abs(zeros - ones)} bit")
    
    # 🔧 DÜZELTME 1: 0 + 1 = total_bits kontrolü
    sonuclar.append(f"Kontrol (0 + 1)    : {zeros + ones} bit")
    if zeros + ones == total_bits:
        sonuclar.append("Bit sayımı tutarlılığı: BAŞARILI")
    else:
        sonuclar.append("Bit sayımı tutarlılığı: HATALI")
    
    sonuclar.append("-" * 30)
    sonuclar.append(f"Hesaplanan Entropi : {entropy:.6f} bit/byte")
    sonuclar.append("İdeal Entropi      : 8.000000 bit/byte")
    
    # 🔧 DÜZELTME 2: Küçük veri uyarısı
    if total_bytes < 1024:
        sonuclar.append("UYARI: Entropi için veri miktarı düşük olabilir")
    
    sonuclar.append("-" * 30)
    
    if 7.9 < entropy <= 8.0:
        sonuclar.append("SONUÇ: Yüksek rastgelelik düzeyi (Başarılı)")
    else:
        sonuclar.append("SONUÇ: Rastgelelik düzeyi yetersiz olabilir")

    # Ekrana yaz
    output_text = "\n".join(sonuclar)
    print(output_text)
    
    # Dosyaya kaydet
    os.makedirs("outputs", exist_ok=True)
    output_file = os.path.join("outputs", "bit_statistics.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output_text)

    print(f"\nSonuçlar kaydedildi: {output_file}")

if __name__ == "__main__":
    target_file = os.path.join("outputs", "random_bits.txt")
    analiz_et(target_file)

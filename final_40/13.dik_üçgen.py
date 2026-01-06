# 1. Adım: Fonksiyonumuzu tanımlıyoruz
def dik_ucgen_alani(taban, yukseklik):
    # Alan hesaplama formülü
    alan = (taban * yukseklik) / 2
    
    # Sonucu dışarıya 'geri döndürüyoruz'
    # return, fonksiyonun işini bitirdiği ve sonucu teslim ettiği yerdir.
    return alan

# --- Fonksiyonun Kullanımı ---

# Kullanıcıdan değerleri alalım
k_uzunlugu = float(input("Taban uzunluğunu giriniz: "))
h_yukseklik = float(input("Yüksekliği giriniz: "))

# Fonksiyonu çağırıyoruz ve dönen sonucu bir değişkene hapsediyoruz
hesaplanan_alan = dik_ucgen_alani(k_uzunlugu, h_yukseklik)

# Sonucu ekrana yazdırıyoruz
print(f"Dik üçgenin alanı: {hesaplanan_alan}")

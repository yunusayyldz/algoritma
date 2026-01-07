def dik_ucgen_alani(taban, yukseklik):

    alan = (taban * yukseklik) / 2
    
    return alan

k_uzunlugu = float(input("Taban uzunluğunu giriniz: "))
h_yukseklik = float(input("Yüksekliği giriniz: "))

hesaplanan_alan = dik_ucgen_alani(k_uzunlugu, h_yukseklik)

print(f"Dik üçgenin alanı: {hesaplanan_alan}")

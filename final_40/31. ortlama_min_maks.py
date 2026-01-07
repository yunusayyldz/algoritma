def liste_istatistikleri(sayi_listesi):

    if len(sayi_listesi) == 0:
        return 0, 0, 0

    en_kucuk = min(sayi_listesi)
    
    en_buyuk = max(sayi_listesi)
    
    toplam = sum(sayi_listesi)
    adet = len(sayi_listesi)
    ortalama = toplam / adet

    return ortalama, en_kucuk, en_buyuk

veri = input("Sayıları aralarında boşluk bırakarak giriniz: ")

liste = list(map(int, veri.split()))

ort, mn, mx = liste_istatistikleri(liste)

print("-" * 30)
print(f"Liste: {liste}")
print(f"Ortalama : {ort:.2f}") # Virgülden sonra 2 basamak
print(f"Minimum  : {mn}")
print(f"Maksimum : {mx}")

def liste_istatistikleri(sayi_listesi):
    # Hata önleme: Eğer liste boşsa işlem yapma
    if len(sayi_listesi) == 0:
        return 0, 0, 0

    # 1. En küçük değeri bulma
    en_kucuk = min(sayi_listesi)
    
    # 2. En büyük değeri bulma
    en_buyuk = max(sayi_listesi)
    
    # 3. Ortalamayı hesaplama (Toplam / Adet)
    toplam = sum(sayi_listesi)
    adet = len(sayi_listesi)
    ortalama = toplam / adet
    
    # Üç değeri birden döndürüyoruz
    return ortalama, en_kucuk, en_buyuk

# --- Ana Program ---

# Kullanıcıdan sayıları alıyoruz (Örn: 10 20 5 40)
veri = input("Sayıları aralarında boşluk bırakarak giriniz: ")

# Girilen metni parçalayıp tam sayı listesine çeviriyoruz
# split() -> boşluklardan böler
# map(int, ...) -> hepsini int'e çevirir
liste = list(map(int, veri.split()))

# Fonksiyonu çağırıp sonuçları alıyoruz
ort, mn, mx = liste_istatistikleri(liste)

print("-" * 30)
print(f"Liste: {liste}")
print(f"Ortalama : {ort:.2f}") # Virgülden sonra 2 basamak
print(f"Minimum  : {mn}")
print(f"Maksimum : {mx}")

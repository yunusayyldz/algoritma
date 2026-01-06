#round = yuvarlama
def benim_yuvarlama(sayi):
    # Eğer sayı pozitifse 0.5 ekleyip tam kısmını alırız
    if sayi >= 0:
        sonuc = int(sayi + 0.5)
    # Eğer sayı negatifse 0.5 çıkarıp tam kısmını alırız
    else:
        sonuc = int(sayi - 0.5)
        
    return sonuc

# --- Test Edelim ---
# Kullanıcıdan ondalıklı (float) bir sayı alıyoruz
girilen_sayi = float(input("Yuvarlanacak sayıyı giriniz: "))

yeni_hali = benim_yuvarlama(girilen_sayi)

print(f"Orijinal: {girilen_sayi}")
print(f"Yuvarlanmış Hali: {yeni_hali}")

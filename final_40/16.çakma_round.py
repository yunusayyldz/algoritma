def benim_yuvarlama(sayi):

    if sayi >= 0:
        sonuc = int(sayi + 0.5)

    else:
        sonuc = int(sayi - 0.5)
        
    return sonuc

girilen_sayi = float(input("Yuvarlanacak sayıyı giriniz: "))

yeni_hali = benim_yuvarlama(girilen_sayi)

print(f"Orijinal: {girilen_sayi}")
print(f"Yuvarlanmış Hali: {yeni_hali}")

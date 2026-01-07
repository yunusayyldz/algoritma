def sayilari_topla(bitis_sayisi):

    toplam = 0
    
    for sayi in range(1, bitis_sayisi + 1):
        toplam += sayi  
        
    return toplam

kullanici_sayisi = int(input("Kaça kadar toplamak istersiniz? : "))

sonuc = sayilari_topla(kullanici_sayisi)

print(f"1'den {kullanici_sayisi} sayısına kadar olanların toplamı: {sonuc}")

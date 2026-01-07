def en_buyuk_boleni_bul(sayi):

    if sayi <= 1:
        return "1'den büyük bir sayı girilmelidir."

    baslangic = sayi // 2
    
    for i in range(baslangic, 0, -1):
        
        if sayi % i == 0:
            return i

girdi = int(input("Bir sayı giriniz: "))

sonuc = en_buyuk_boleni_bul(girdi)

print(f"{girdi} sayısının kendisi hariç en büyük böleni: {sonuc}")

def tekrar_edenleri_bul(liste):
    gorulenler = set()
    tekrar_edenler = set()
    
    for eleman in liste:

        if eleman in gorulenler:
            tekrar_edenler.add(eleman)
        else:

            gorulenler.add(eleman)
            
    return list(tekrar_edenler)


veri = input("Elemanları aralarında boşluk bırakarak giriniz: ")
orijinal_liste = veri.split() 

sonuc = tekrar_edenleri_bul(orijinal_liste)

if len(sonuc) > 0:
    print(f"Tekrar eden elemanlar: {sonuc}")
else:
    print("Hiçbir eleman tekrar etmiyor.")

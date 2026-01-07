def asal_sayilari_bul(sinir):

    asal_listesi = []
    
    for sayi in range(2, sinir + 1):
        

        asal_mi = True

        limit = int(sayi ** 0.5) + 1
        
        for i in range(2, limit):
            if sayi % i == 0:
                asal_mi = False
                break  

        if asal_mi:
            asal_listesi.append(sayi)
            
    return asal_listesi

girilen_sinir = int(input("Kaça kadar olan asal sayıları bulalım?: "))

sonuc = asal_sayilari_bul(girilen_sinir)

print(f"\n2 ile {girilen_sinir} arasındaki asal sayılar:")
print(sonuc)
print(f"\nToplam {len(sonuc)} adet asal sayı bulundu.")

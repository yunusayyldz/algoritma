def tekrar_edenleri_bul(liste):
    gorulenler = set()
    tekrar_edenler = set()
    
    for eleman in liste:
        # Eğer bu elemanı daha önce gördüysek, bu bir kopyadır
        if eleman in gorulenler:
            tekrar_edenler.add(eleman)
        else:
            # İlk kez görüyorsak, görülenler listesine ekle
            gorulenler.add(eleman)
            
    return list(tekrar_edenler)

# --- Ana Program ---
veri = input("Elemanları aralarında boşluk bırakarak giriniz: ")
orijinal_liste = veri.split() # Girişi listeye çevir

sonuc = tekrar_edenleri_bul(orijinal_liste)

if len(sonuc) > 0:
    print(f"Tekrar eden elemanlar: {sonuc}")
else:
    print("Hiçbir eleman tekrar etmiyor.")

def asal_sayilari_bul(sinir):
    # Asal sayıları biriktireceğimiz boş liste
    asal_listesi = []
    
    # 1. DIŞ DÖNGÜ: 2'den başlayıp sınıra kadar sayıları geziyoruz
    for sayi in range(2, sinir + 1):
        
        # Başlangıçta bu sayıyı asal kabul ediyoruz
        asal_mi = True
        
        # 2. İÇ DÖNGÜ: Asallık Kontrolü (Önceki örneğimizdeki mantık)
        # Sayının kareköküne kadar bölen var mı diye bakıyoruz
        limit = int(sayi ** 0.5) + 1
        
        for i in range(2, limit):
            if sayi % i == 0:
                asal_mi = False
                break  # Bölen bulundu, asal değil, iç döngüyü kır.
        
        # 3. KARAR: Eğer döngü bittiğinde hala asalsa listeye ekle
        if asal_mi:
            asal_listesi.append(sayi)
            
    return asal_listesi

# --- Ana Program ---
girilen_sinir = int(input("Kaça kadar olan asal sayıları bulalım?: "))

sonuc = asal_sayilari_bul(girilen_sinir)

print(f"\n2 ile {girilen_sinir} arasındaki asal sayılar:")
print(sonuc)
print(f"\nToplam {len(sonuc)} adet asal sayı bulundu.")

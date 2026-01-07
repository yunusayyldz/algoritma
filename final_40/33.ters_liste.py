def tersine_cevir_manuel(liste):
    yeni_liste = []

    for i in range(len(liste) - 1, -1, -1):
        eleman = liste[i]
        yeni_liste.append(eleman)
        
    return yeni_liste


veri = input("Sayıları aralarında boşluk bırakarak giriniz: ")

orijinal_liste = list(map(int, veri.split()))

ters_liste = tersine_cevir_manuel(orijinal_liste)

print("-" * 30)
print(f"Orijinal : {orijinal_liste}")
print(f"Ters Hali: {ters_liste}")

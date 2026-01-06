def tersine_cevir_manuel(liste):
    yeni_liste = []
    
    # range(başlangıç, bitiş, adım)
    # Başlangıç: len(liste) - 1 (Listenin son indeksi)
    # Bitiş: -1 (0. indekse kadar gitmek için -1 veriyoruz)
    # Adım: -1 (Geri geri git)
    for i in range(len(liste) - 1, -1, -1):
        eleman = liste[i]
        yeni_liste.append(eleman)
        
    return yeni_liste

# --- Kullanıcıdan Veri Alma ---
veri = input("Sayıları aralarında boşluk bırakarak giriniz: ")
# Girilen metni sayı listesine çeviriyoruz
orijinal_liste = list(map(int, veri.split()))

# Fonksiyonu çağır
ters_liste = tersine_cevir_manuel(orijinal_liste)

print("-" * 30)
print(f"Orijinal : {orijinal_liste}")
print(f"Ters Hali: {ters_liste}")

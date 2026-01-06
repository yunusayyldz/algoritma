# 1. Adım: Kullanıcıdan metni alıyoruz
metin = input("Lütfen bir metin giriniz: ")

print("--- İndis Numaraları ve Harfler ---")

# 2. Adım: enumerate fonksiyonu ile hem sırayı hem harfi alıyoruz
# 'sira' değişkeni numarayı (0, 1, 2...), 'karakter' değişkeni harfi tutar.
for sira, karakter in enumerate(metin):
    # f-string yapısı (f"...") ile değişkenleri metin içine kolayca yerleştiriyoruz.
    print(f"{sira} -> {karakter}")

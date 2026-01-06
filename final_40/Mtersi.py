# 1. Adım: Kullanıcıdan metni alıyoruz
girilen_metin = input("Lütfen bir metin giriniz: ")

# 2. Adım: Metni terse çeviriyoruz
# [::-1] ifadesi Python'a özel bir kısayoldur.
ters_metin = girilen_metin[::-1]

# 3. Adım: Sonucu ekrana yazdırıyoruz
print("Metnin ters hali:", ters_metin)

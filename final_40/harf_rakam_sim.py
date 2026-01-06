# 1. Adım: Kullanıcıdan karakteri alıyoruz
veri = input("Lütfen klavyeden bir tuşa basınız (Tek karakter): ")

# 2. Adım: Karakterin türünü kontrol ediyoruz

# .isalpha() -> "Alphabet" kelimesinden gelir. "Bu bir harf mi?" diye sorar.
if veri.isalpha():
    print("Girdiğiniz karakter bir HARF'tir.")

# .isdigit() -> "Digit" kelimesinden gelir. "Bu bir rakam mı?" diye sorar.
elif veri.isdigit():
    print("Girdiğiniz karakter bir RAKAM'dır.")

# Yukarıdakilerin hiçbiri değilse, geriye simge kalır.
else:
    print("Girdiğiniz karakter bir SİMGE'dir.")

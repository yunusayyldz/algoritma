# 1. Adım: Kullanıcıdan metni alıyoruz
girilen_metin = input("Lütfen bir metin giriniz: ")

# 2. Adım: Büyük/Küçük harfleri birbirine dönüştürüyoruz
# swapcase() komutu bu takas işlemini otomatik yapar.
donusturulmus_metin = girilen_metin.swapcase()

# 3. Adım: Sonucu ekrana yazdırıyoruz
print("Dönüştürülmüş hali:", donusturulmus_metin)

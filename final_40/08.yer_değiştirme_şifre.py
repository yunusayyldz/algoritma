metin = input("giriniz")

şifreli = ""

for i in range(0, len(metin)-1,2):
    şifreli += metin[i+1] + metin[i]
if len(metin) % 2 != 0:
    şifreli += metin[-1]
    
print("orjinal",metin)
print("şifreli",şifreli)







# 1. Adım: Metni alıyoruz
metin = input("Şifrelenecek metni giriniz: ")

# Şifrelenmiş halini tutacağımız boş bir kutu (değişken) oluşturuyoruz
sifreli_metin = ""

# 2. Adım: İkişer ikişer atlayarak döngü kuruyoruz
# range(başlangıç, bitiş, adım_sayısı)
# len(metin) - 1 dedik çünkü son harf tek kalırsa hata vermesin, onu döngü dışında halledeceğiz.
for i in range(0, len(metin) - 1, 2):
    # i -> O anki harfin sırası
    # i+1 -> Yanındaki harfin sırası
    
    # Önce yanındakini (i+1), sonra kendisini (i) alıp ekliyoruz.
    sifreli_metin += metin[i+1] + metin[i]

# 3. Adım: Metin uzunluğu tek sayı mı diye kontrol ediyoruz
if len(metin) % 2 != 0:
    # Eğer tek sayıysa, en sondaki harf işlem görmedi demektir.
    # Onu da olduğu gibi sona ekliyoruz.
    sifreli_metin += metin[-1]

# 4. Adım: Sonucu yazdırıyoruz
print("Orijinal Metin:", metin)
print("Şifreli Metin :", sifreli_metin)




# 1 - sayıyı metne çevirme 

birler = ["","bir","iki","üç"]
onlar = ["","on","yirmi","otuz"]

sayi = int(input("değiştirmek istediğiniz sayıyı giriniz:"))

num1 = sayi // 10
num2 = sayi % 10

print(onlar[num1], birler[num2])

# 2 - harf rakam simge bulan program

veri  = input("giriniz")

if veri.isalpha():
    print("harf")
elif veri.isdigit():
    print("rakam")
else:
    print("simge")

# 3 - sesli harf bulma

sesli_harf = "aeıiuüoöAEIİUÜOÖ"
sayaç = 0 
cümle = input("harf alalım :")
for harf in cümle :
    if harf in sesli_harf :
        sayaç += 1 
print("toplam sesli harf sayısı",sayaç)

# 4 - metnin tersini verme 

girilen_metin = input("tersine dönmesini istediğiniz metni girin:")
ters_metin = girilen_metin[::-1]
print("ters metin",ters_metin)

# 5 - girilen harfi büyükse küçük küçükse büyük yapma 

girilen_metin = input("buyrunuz:")

değişen_metin = girilen_metin.swapcase()
print("yeni gibi oldu:",değişen_metin)

# 6 - türkçe girilen metni altin alfaebsine göre yazma

ceviri_tablosu = {
    "ç": "c", "Ç": "C",
    "ğ": "g", "Ğ": "G",
    "ı": "i", "İ": "I",
    "ö": "o", "Ö": "O",
    "ş": "s", "Ş": "S",
    "ü": "u", "Ü": "U"
}

metin = input("Lütfen Türkçe karakter içeren bir metin giriniz: ")

for turkce, latin in ceviri_tablosu.items():
    metin = metin.replace(turkce, latin)

print("Dönüştürülmüş hali:", metin)

# 7 - girilen metni her bir harfe sayı atayarak sırlama yapma programı

metin = input("Lütfen bir metin giriniz: ")

print("--- İndis Numaraları ve Harfler ---")

for sira, karakter in enumerate(metin):

    print(f"{sira} -> {karakter}")

# 8 - şiferleme

metin = input("Şifrelenecek metni giriniz: ")

sifreli_metin = ""

for i in range(0, len(metin) - 1, 2):

    sifreli_metin += metin[i+1] + metin[i]

if len(metin) % 2 != 0:

    sifreli_metin += metin[-1]

print("Orijinal Metin:", metin)
print("Şifreli Metin :", sifreli_metin)

# 9 - sansür

metin = input("Şifrelenecek metni giriniz: ")

sifreli_metin = ""

for i in range(0, len(metin) - 1, 2):

    sifreli_metin += metin[i+1] + metin[i]

if len(metin) % 2 != 0:

    sifreli_metin += metin[-1]

print("Orijinal Metin:", metin)
print("Şifreli Metin :", sifreli_metin)

# 10 - a yı bulma

metin = input("Lütfen bir cümle giriniz: ").lower()

kelimeler = metin.split()

sayac = 0

for kelime in kelimeler:
    
    if "a" in kelime:
        sayac += 1 
        
print(f"İçinde 'a' harfi geçen kelime sayısı: {sayac}")

# 11 - tahmin

import random 

puan = 0 

while puan < 5:

    gizli_sayi = random.randint(1, 5)
    
    tahmin = int(input(f"Puanın {puan}. Tahminin (1-5 arası): "))
    
    if tahmin == gizli_sayi:
        puan += 1  
        print("Tebrikler! Doğru bildin.")
    else:
        print(f"Maalesef... Tuttuğum sayı {gizli_sayi} idi.")
    
    print("-" * 20) 

print("\nOyun Bitti! Toplam 5 puana ulaştın, şampiyonsun!")

# 12 - bankot

banknot = [200, 100, 50, 20, 10, 5, 1]

para = int(input("Lütfen para miktarını giriniz: "))

for değer in banknot:

    adet = para // değer

    if adet > 0:
        print(adet,"x",değer)
        
        para = para % değer

# 13 - 

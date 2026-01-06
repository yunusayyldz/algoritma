# 1 - sayıyı metne çevirme 
"""
birler = ["","bir","iki","üç"]
onlar = ["","on","yirmi","otuz"]

sayi = int(input("değiştirmek istediğiniz sayıyı giriniz:"))

num1 = sayi // 10
num2 = sayi % 10

print(onlar[num1], birler[num2])
"""
# 2 - harf rakam simge bulan program
"""
veri  = input("giriniz")

if veri.isalpha():
    print("harf")
elif veri.isdigit():
    print("rakam")
else:
    print("simge")
"""
# 3 - sesli harf bulma
"""
sesli_harf = "aeıiuüoöAEIİUÜOÖ"
sayaç = 0 
cümle = input("harf alalım :")
for harf in cümle :
    if harf in sesli_harf :
        sayaç += 1 
print("toplam sesli harf sayısı",sayaç)
"""
# 4 - metnin tersini verme 
"""
girilen_metin = input("tersine dönmesini istediğiniz metni girin:")
ters_metin = girilen_metin[::-1]
print("ters metin",ters_metin)
"""
# 5 - girilen harfi büyükse küçük küçükse büyük yapma 
"""
girilen_metin = input("buyrunuz:")

değişen_metin = girilen_metin.swapcase()
print("yeni gibi oldu:",değişen_metin)
"""
# 6 - türkçe girilen metni altin alfaebsine göre yazma
"""
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
"""
# 7 - girilen metni her bir harfe sayı atayarak sırlama yapma programı
"""
metin = input("Lütfen bir metin giriniz: ")

print("--- İndis Numaraları ve Harfler ---")

for sira, karakter in enumerate(metin):

    print(f"{sira} -> {karakter}")
"""
# 8 - şiferleme
"""
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
"""
# 9 - sansür
"""# 1. Adım: Metni alıyoruz
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
"""
# 10 - a yı bulma
"""
# 1. Adım: Kullanıcıdan cümleyi alıyoruz
# .lower() ekledik ki büyük 'A' içeren kelimeleri de (örneğin 'Ankara') kaçırmayalım.
metin = input("Lütfen bir cümle giriniz: ").lower()

# 2. Adım: Cümleyi kelimelere ayırıyoruz
kelimeler = metin.split()

# Sayacımızı sıfırlıyoruz
sayac = 0

# 3. Adım: Kelimeleri tek tek kontrol ediyoruz
for kelime in kelimeler:
    # Python'da "in" kelimesi "içinde var mı?" sorusunu sorar.
    if "a" in kelime:
        sayac += 1  # Varsa sayacı artır

# 4. Adım: Sonucu yazdırıyoruz
print(f"İçinde 'a' harfi geçen kelime sayısı: {sayac}")
"""
# 11 - tahmin
"""
import random  # Rastgele sayı üretmek için gerekli kütüphane

puan = 0  # Başlangıç puanımız

print("--- Sayı Tahmin Oyunu Başladı! ---")
print("Hedef: 5 puan toplamak.\n")

# Puan 5'ten küçük olduğu sürece bu döngü dönmeye devam eder.
while puan < 5:
    # 1. Adım: Bilgisayar 1-5 arası sayı tutar
    gizli_sayi = random.randint(1, 5)
    
    # 2. Adım: Kullanıcıdan tahmin istenir
    # input'u int() ile tam sayıya çeviriyoruz.
    tahmin = int(input(f"Puanın {puan}. Tahminin (1-5 arası): "))
    
    # 3. Adım: Kontrol
    if tahmin == gizli_sayi:
        puan += 1  # Puanı 1 artır
        print("Tebrikler! Doğru bildin.")
    else:
        print(f"Maalesef... Tuttuğum sayı {gizli_sayi} idi.")
    
    print("-" * 20)  # Görsel olarak turları ayırmak için çizgi

# Döngü bittiğinde burası çalışır
print("\nOyun Bitti! Toplam 5 puana ulaştın, şampiyonsun!")
"""
# 12 - bankot
"""
# 1. Adım: Banknotlarımızı tanımlıyoruz
# Büyükten küçüğe sıralamak ZORUNLUDUR.
# En sona 1 ekledik ki bozuk paraları da hesaplayabilsin.
banknot_listesi = [200, 100, 50, 20, 10, 5, 1]

# 2. Adım: Kullanıcıdan para miktarını alıyoruz
para = int(input("Lütfen para miktarını giriniz: "))

print(f"\n--- {para} TL için Banknot Dağılımı ---")

# 3. Adım: Her bir banknotu sırasıyla deniyoruz
for banknot in banknot_listesi:
    # Bu banknottan kaç tane verebiliriz? (Tam bölme)
    adet = para // banknot
    
    # Eğer bu banknottan en az 1 tane verebiliyorsak:
    if adet > 0:
        print(f"{adet} x {banknot} TL")
        
        # Verdiğimiz miktarı ana paradan düşüyoruz (Kalanı buluyoruz)
        para = para % banknot

# İşlem bittiğinde 'para' değişkeni 0 olur.
"""
# 13 - 

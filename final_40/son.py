"""
YUNUS AYYILDIZ - ALGORİTMA DERSİ
FINAL_40 KLASÖRÜ - HİBRİT YAPI
(01-15: Orijinal/Tam İçerik | 16-40: Gruplandırılmış/Kısa İçerik)
"""

# =============================================================================
# BÖLÜM 1: İLK 15 SORU (ORİJİNAL, BOZULMAMIŞ HALİ)
# =============================================================================

# -----------------------------------------------------------------------------
# 01. Sayı > Kelime
# -----------------------------------------------------------------------------
birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar  = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

girilen_sayi = int(input("Lütfen iki basamaklı bir sayı giriniz: "))

onlar_basamagi = girilen_sayi // 10  
birler_basamagi = girilen_sayi % 10  

print(onlar[onlar_basamagi] + " " + birler[birler_basamagi])


# -----------------------------------------------------------------------------
# 02. Harf Rakam Simge
# -----------------------------------------------------------------------------
veri = input("Lütfen klavyeden bir tuşa basınız (Tek karakter): ")

if veri.isalpha():
    print("Girdiğiniz karakter bir HARF'tir.")

elif veri.isdigit():
    print("Girdiğiniz karakter bir RAKAM'dır.")

else:
    print("Girdiğiniz karakter bir SİMGE'dir.")


# -----------------------------------------------------------------------------
# 03. Sesli Harf Sayacı
# -----------------------------------------------------------------------------
# 1. Adım: Hangi harfleri aradığımızı tanımlıyoruz
# Hem küçük hem büyük harfleri yazdık ki hatasız bulsun.
sesli_harfler = "aeıioöuüAEIİOÖUÜ"

# 2. Adım: Sayacı hazırlıyoruz (Başlangıçta 0)
sayac = 0

# 3. Adım: Kullanıcıdan cümleyi alıyoruz
cumle = input("Lütfen bir cümle giriniz: ")

# 4. Adım: Cümlenin içindeki her harfi tek tek geziyoruz
for harf in cumle:
    # Eğer o anki harf, sesli_harfler listemizin içindeyse;
    if harf in sesli_harfler:
        sayac += 1  # Sayacı 1 artır

# 5. Adım: Sonucu yazdırıyoruz
print("Bu cümledeki sesli harf sayısı:", sayac)


# -----------------------------------------------------------------------------
# 04. Metni Terse Çevirme
# -----------------------------------------------------------------------------
# 1. Adım: Kullanıcıdan metni alıyoruz
girilen_metin = input("Lütfen bir metin giriniz: ")

# 2. Adım: Metni terse çeviriyoruz
# [::-1] ifadesi Python'a özel bir kısayoldur.
ters_metin = girilen_metin[::-1]

# 3. Adım: Sonucu ekrana yazdırıyoruz
print("Metnin ters hali:", ters_metin)


# -----------------------------------------------------------------------------
# 05. Büyük/Küçük Harf Dönüşümü
# -----------------------------------------------------------------------------
# 1. Adım: Kullanıcıdan metni alıyoruz
girilen_metin = input("Lütfen bir metin giriniz: ")

# 2. Adım: Büyük/Küçük harfleri birbirine dönüştürüyoruz
# swapcase() komutu bu takas işlemini otomatik yapar.
donusturulmus_metin = girilen_metin.swapcase()

# 3. Adım: Sonucu ekrana yazdırıyoruz
print("Dönüştürülmüş hali:", donusturulmus_metin)


# -----------------------------------------------------------------------------
# 06. Latin Karakter Dönüşümü
# -----------------------------------------------------------------------------
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


# -----------------------------------------------------------------------------
# 07. İndis Numaralandırma
# -----------------------------------------------------------------------------
# 1. Adım: Kullanıcıdan metni alıyoruz
metin = input("Lütfen bir metin giriniz: ")

print("--- İndis Numaraları ve Harfler ---")

# 2. Adım: enumerate fonksiyonu ile hem sırayı hem harfi alıyoruz
# 'sira' değişkeni numarayı (0, 1, 2...), 'karakter' değişkeni harfi tutar.
for sira, karakter in enumerate(metin):
    # f-string yapısı (f"...") ile değişkenleri metin içine kolayca yerleştiriyoruz.
    print(f"{sira} -> {karakter}")


# -----------------------------------------------------------------------------
# 08. Yer Değiştirme Şifrelemesi
# -----------------------------------------------------------------------------
metin = input("giriniz")

şifreli = ""

for i in range(0, len(metin)-1,2):
    şifreli += metin[i+1] + metin[i]
if len(metin) % 2 != 0:
    şifreli += metin[-1]
    
print("orjinal",metin)
print("şifreli",şifreli)

# --- (Dosyadaki İkinci Çözüm) ---

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


# -----------------------------------------------------------------------------
# 09. Sansürleme
# -----------------------------------------------------------------------------
metin = input("buyrun: ")

yeni = []
for kelime in metin.split():
    ilk = kelime[0]
    yıldız = "*" * (len(kelime)-1)
    maske = ilk + yıldız
     
    yeni.append(maske)
    
sonuç = "".join(yeni)
print(sonuç)


# -----------------------------------------------------------------------------
# 10. 'a' Harfi Bulma
# -----------------------------------------------------------------------------
metin = input("Lütfen bir cümle giriniz: ")

sayac = 0

for kelime in metin.split():
    
    if "a" in kelime or "A" in kelime :
        sayac += 1  

print(f"İçinde 'a' harfi geçen kelime sayısı: {sayac}")


# -----------------------------------------------------------------------------
# 11. Sayı Tahmin Oyunu
# -----------------------------------------------------------------------------
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


# -----------------------------------------------------------------------------
# 12. Banknot (Para Üstü) Hesaplama
# -----------------------------------------------------------------------------
banknot = [200, 100, 50, 20, 10, 5, 1]

para = int(input("Lütfen para miktarını giriniz: "))

for değer in banknot:

    adet = para // değer

    if adet > 0:
        print(adet,"x",değer)
        
        para = para % değer


# -----------------------------------------------------------------------------
# 13. Dik Üçgen Alanı
# -----------------------------------------------------------------------------
def dik_ucgen_alani(taban, yukseklik):

    alan = (taban * yukseklik) / 2
    
    return alan

k_uzunlugu = float(input("Taban uzunluğunu giriniz: "))
h_yukseklik = float(input("Yüksekliği giriniz: "))

hesaplanan_alan = dik_ucgen_alani(k_uzunlugu, h_yukseklik)

print(f"Dik üçgenin alanı: {hesaplanan_alan}")


# -----------------------------------------------------------------------------
# 14. Üçgen Alanı (Sinüs Teoremi)
# -----------------------------------------------------------------------------
import math 

a = float(input("Birinci kenar uzunluğunu (a) giriniz: "))
b = float(input("İkinci kenar uzunluğunu (b) giriniz: "))
aci = float(input("Aradaki açıyı (derece olarak) giriniz: "))

alan = a * b * math.sin(aci * math.pi / 180) / 2

print(f"Üçgenin Alanı: {alan:.2f}")


# -----------------------------------------------------------------------------
# 15. Güçlü Şifre Kontrolü
# -----------------------------------------------------------------------------
# 1. Adım: Kullanıcıdan şifreyi alıyoruz
sifre = input("Lütfen şifrenizi giriniz: ")

# 2. Adım: Kontrol bayraklarını hazırlıyoruz (Başlangıçta hiçbiri yok)
buyuk_var = False
kucuk_var = False
rakam_var = False
simge_var = False

# Özel karakterlerin ne olduğunu tanımlayalım
simgeler = "!@#$%^&*()_+-=[]{}|;':,.<>/?\\"

# 3. Adım: Şifredeki her karakteri tek tek kontrol ediyoruz
for karakter in sifre:
    if karakter.isupper():       # Büyük harf mi?
        buyuk_var = True
    elif karakter.islower():     # Küçük harf mi?
        kucuk_var = True
    elif karakter.isdigit():     # Rakam mı?
        rakam_var = True
    elif karakter in simgeler:   # Listemizdeki simgelerden biri mi?
        simge_var = True

# 4. Adım: Puanı hesaplıyoruz
# Python'da True = 1, False = 0 demektir. Bunları toplayabiliriz.
toplam_puan = int(buyuk_var) + int(kucuk_var) + int(rakam_var) + int(simge_var)

# 5. Adım: Sonucu ekrana yazdırıyoruz
print(f"Tespit edilen özellik sayısı: {toplam_puan}")

if toplam_puan == 4:
    print("Şifre Durumu: ÇOK GÜÇLÜ")
elif toplam_puan == 3:
    print("Şifre Durumu: GÜÇLÜ")
elif toplam_puan == 2:
    print("Şifre Durumu: ORTA")
elif toplam_puan <= 1:
    print("Şifre Durumu: ZAYIF")


# =============================================================================
# BÖLÜM 2: 16-40 ARASI (GRUPLANDIRILMIŞ VE KISALTILMIŞ)
# =============================================================================

# --- MATEMATİK VE SAYI İŞLEMLERİ ---

# 16. Manuel Yuvarlama
s = float(input("Sayı: "))
print(int(s + 0.5) if s >= 0 else int(s - 0.5))

# 17. 1'den N'e Toplam
print(sum(range(1, int(input("Kaça kadar: ")) + 1)))

# 18. EBOB ve EKOK
s1, s2 = int(input("S1: ")), int(input("S2: "))
a, b = s1, s2
while b: a, b = b, a % b
print(f"EBOB: {a}, EKOK: {(s1*s2)//a}")

# 19. Faktöriyel (Recursive)
def fak(n): return 1 if n < 2 else n * fak(n-1)
print(fak(int(input("Sayı: "))))

# 20. Kendisi Hariç En Büyük Bölen
s = int(input("Sayı: "))
for i in range(s//2, 0, -1):
    if s % i == 0: print(i); break

# 21. Decimal -> Binary
s, b = int(input("Sayı: ")), ""
while s > 0: b = str(s % 2) + b; s //= 2
print(b or "0")

# 24. 1/x Bölme
s = float(input("Sayı: "))
print(f"{1/s:.3f}" if s != 0 else "0 bölünmez")

# 26. Maclaurin Sin(x)
import math
x = math.radians(float(input("Derece: ")))
print(sum(((-1)**((n-1)//2)) * (x**n) / math.factorial(n) for n in range(1, 10, 2)))

# 28. Asal Kontrol
s = int(input("Sayı: "))
print("Asal" if s > 1 and all(s % i != 0 for i in range(2, int(s**0.5)+1)) else "Değil")

# 30. Asal Liste
limit = int(input("Sınır: "))
print([s for s in range(2, limit + 1) if all(s % i != 0 for i in range(2, int(s**0.5)+1))])

# 34. Mükemmel Sayı
s = int(input("Sayı: "))
print("Mükemmel" if s > 1

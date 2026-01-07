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

sayac = 0

cumle = input("Lütfen bir cümle giriniz: ")

for harf in cumle:

    if harf in sesli_harfler:
        sayac += 1 

print("Bu cümledeki sesli harf sayısı:", sayac)


# -----------------------------------------------------------------------------
# 04. Metni Terse Çevirme
# -----------------------------------------------------------------------------
# 1. Adım: Kullanıcıdan metni alıyoruz
girilen_metin = input("Lütfen bir metin giriniz: ")

ters_metin = girilen_metin[::-1]

print("Metnin ters hali:", ters_metin)


# -----------------------------------------------------------------------------
# 05. Büyük/Küçük Harf Dönüşümü
# -----------------------------------------------------------------------------

girilen_metin = input("Lütfen bir metin giriniz: ")

donusturulmus_metin = girilen_metin.swapcase()

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

for sira, karakter in enumerate(metin):

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
import random 

puan = 0 

print("--- Sayı Tahmin Oyunu Başladı! ---")
print("Hedef: 5 puan toplamak.\n")

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

buyuk_var = False
kucuk_var = False
rakam_var = False
simge_var = False

simgeler = "!@#$%^&*()_+-=[]{}|;':,.<>/?\\"

for karakter in sifre:
    if karakter.isupper():       
        buyuk_var = True
    elif karakter.islower():     
        kucuk_var = True
    elif karakter.isdigit():     
        rakam_var = True
    elif karakter in simgeler:   
        simge_var = True

toplam_puan = int(buyuk_var) + int(kucuk_var) + int(rakam_var) + int(simge_var)

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
print("Mükemmel" if s > 1 and sum(i for i in range(1, s//2 + 1) if s % i == 0) == s else "Değil")

# 39. Armstrong Sayısı
s = input("Sayı: ")
print("Armstrong" if sum(int(d)**len(s) for d in s) == int(s) else "Değil")


# --- LİSTE VE İSTATİSTİK İŞLEMLERİ ---

# 22. Onlar Basamağı Toplama
print(sum(((int(input(f"{i}. sayı: ")) // 10) % 10) * 10 for i in range(1, 11)))

# 23. En Büyük Sayı
print("En büyük:", max(int(input(f"{i}. sayı: ")) for i in range(1, 11)))

# 31. Liste İstatistik
L = list(map(int, input("Sayılar: ").split()))
print(f"Ort: {sum(L)/len(L):.2f}, Min: {min(L)}, Max: {max(L)}")

# 33. Ters Liste
L = input("Liste: ").split()
print([L[i] for i in range(len(L)-1, -1, -1)])

# 35. Kesişim Birleşim
s1, s2 = set([1,2,3,4,5]), set([4,5,6,7,8])
print(f"Kesişim: {s1 & s2}, Birleşim: {s1 | s2}")

# 36. Tekrar Edenler
L = input("Veri: ").split()
print(set([x for x in L if L.count(x) > 1]))

# 38. Not Ortalaması
n = [float(input(f"{i+1}. Not: ")) for i in range(int(input("Kaç öğrenci: ")))]
print(f"Ort: {sum(n)/len(n):.2f}, Max: {max(n)}, Min: {min(n)}")

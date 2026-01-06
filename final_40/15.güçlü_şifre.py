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

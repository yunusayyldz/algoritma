def sifrele(metin, anahtar):
    sonuc = ""
    for harf in metin:
        if harf.isalpha():
            baslangic = 65 if harf.isupper() else 97
            yeni_kod = (ord(harf) - baslangic + anahtar) % 26 + baslangic
            sonuc += chr(yeni_kod)
        else:
            sonuc += harf
    return sonuc

def sifre_coz(sifreli_metin, anahtar):
    cozulmus_metin = ""
    for harf in sifreli_metin:
        if harf.isalpha():
            baslangic = 65 if harf.isupper() else 97
            # Çözerken anahtarı çıkarıyoruz (-)
            yeni_kod = (ord(harf) - baslangic - anahtar) % 26 + baslangic
            cozulmus_metin += chr(yeni_kod)
        else:
            cozulmus_metin += harf
    return cozulmus_metin

# --- ANA PROGRAM (KULLANICI GİRİŞİ) ---
print("-" * 30)
print("Sezar Şifreleme Aracına Hoş Geldiniz")
print("1 - Metin Şifrele")
print("2 - Şifre Çöz")
print("-" * 30)

# 1. Adım: Kullanıcıdan seçim al
secim = input("Yapmak istediğiniz işlem (1 veya 2): ")

# 2. Adım: Metni al
metin_girisi = input("Metni giriniz: ")

# 3. Adım: Anahtar sayısını al (Sayıya çevirmeyi unutma!)
anahtar_sayisi = int(input("Anahtar (Kaydırma) sayısı kaç olsun?: "))

print("-" * 30)

if secim == '1':
    # Şifreleme Fonksiyonunu Çağır
    sonuc = sifrele(metin_girisi, anahtar_sayisi)
    print(f"🔒 Şifrelenmiş Sonuç: {sonuc}")
    
elif secim == '2':
    # Çözme Fonksiyonunu Çağır
    sonuc = sifre_coz(metin_girisi, anahtar_sayisi)
    print(f"🔓 Çözülmüş Sonuç: {sonuc}")
    
else:
    print("Hata: Lütfen sadece 1 veya 2 tuşlayınız.")

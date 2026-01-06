""" Basamak Sayısı: 153 sayısı 3 basamaklıdır.
(Demek ki her rakamın 3. kuvvetini yani küpünü alacağız).
Rakamlar: 1, 5 ve 3
Hesaplama:
  1 küpü = 1
  5 küpü = 125
  3 küpü = 27
  Toplam: 1 + 125 + 27 = 153
Sonuç (153), başladığımız sayıya (153) eşit mi? EVET. O halde bu bir Armstrong sayısıdır."""

def armstrong_kontrol(veri):
    # 1. Adım: Negatif sayılarda Armstrong kontrolü yapılmaz
    # (Girdiyi önce string olarak aldığımız için kontrolü sonra yapıyoruz)
    if not veri.isdigit():
        return "Lütfen sadece pozitif tam sayı giriniz."
    
    # 2. Adım: Basamak sayısını (üssü) bul
    basamak_sayisi = len(veri)
    
    toplam = 0
    
    # 3. Adım: Her rakamı gez, üssünü al ve topla
    for rakam in veri:
        # Rakamı string'den integer'a çevirip işlem yapıyoruz
        sayisal_deger = int(rakam)
        
        # Formül: rakam üzeri basamak_sayisi
        toplam += sayisal_deger ** basamak_sayisi
        
    # 4. Adım: Karşılaştırma
    # Toplam, orijinal sayıya (int haline) eşit mi?
    if toplam == int(veri):
        return True
    else:
        return False

# --- Ana Program ---
girilen_sayi = input("Kontrol edilecek sayıyı giriniz: ")

if armstrong_kontrol(girilen_sayi) == True:
    print(f"✅ EVET! {girilen_sayi} bir Armstrong sayısıdır.")
elif armstrong_kontrol(girilen_sayi) == False:
    print(f"❌ HAYIR. {girilen_sayi} bir Armstrong sayısı değildir.")
else:
    # Hatalı giriş uyarısı
    print(armstrong_kontrol(girilen_sayi))

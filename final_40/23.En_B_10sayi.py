print("--- En Büyük Sayıyı Bulma Programı ---")

# 1. Adım: İlk sayıyı alıp "En Büyük" ilan ediyoruz
# Bunu döngüden önce yapıyoruz ki kıyaslayacak bir baz noktamız olsun.
en_buyuk = int(input("1. sayıyı giriniz: "))

# 2. Adım: Geriye kalan 9 sayı için döngü kuruyoruz
# range(2, 11) -> 2'den 10'a kadar (10 dahil) numaralandırmak için.
for i in range(2, 11):
    sayi = int(input(f"{i}. sayıyı giriniz: "))
    
    # 3. Adım: Kıyaslama (Meydan Okuma)
    # Eğer yeni gelen sayı, mevcut 'en_buyuk'ten daha büyükse;
    if sayi > en_buyuk:
        en_buyuk = sayi  # Yeni kral bu sayı olur.

# 4. Adım: Sonucu yazdırıyoruz
print("-" * 30)
print(f"Girdiğiniz sayılar içinde en büyüğü: {en_buyuk}")

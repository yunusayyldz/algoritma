# 1. Adım: Ay isimlerini hafızaya alıyoruz
# Listeyi oluştururken başına boş tırnak "" koyduk.
# Böylece aylar[1] dediğimizde direkt "Ocak" gelecek.
aylar = ["", "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", 
         "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]

# 2. Adım: Kullanıcıdan numarayı alıyoruz
ay_no = int(input("Lütfen ay numarasını (1-12) giriniz: "))

# 3. Adım: Geçerli bir sayı mı diye kontrol ediyoruz
if 1 <= ay_no <= 12:
    
    # Ayın ismini listeden çekiyoruz
    ay_ismi = aylar[ay_no]
    
    # Mevsimi belirliyoruz
    # "in" komutu "bu listenin içinde mi?" diye bakar.
    if ay_no in [12, 1, 2]:
        mevsim = "Kış"
    elif ay_no in [3, 4, 5]:
        mevsim = "İlkbahar"
    elif ay_no in [6, 7, 8]:
        mevsim = "Yaz"
    else:
        mevsim = "Sonbahar"
    
    # 4. Adım: Sonucu istenen formatta yazdırıyoruz
    print(f"{ay_no} -> {ay_ismi} -> {mevsim}")

else:
    # Hatalı giriş yapılırsa
    print("Hata: Lütfen 1 ile 12 arasında bir sayı giriniz!")

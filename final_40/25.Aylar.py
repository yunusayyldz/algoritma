
aylar = ["", "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", 
         "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]

ay_no = int(input("Lütfen ay numarasını (1-12) giriniz: "))

if 1 <= ay_no <= 12:

    ay_ismi = aylar[ay_no]

    if ay_no in [12, 1, 2]:
        mevsim = "Kış"
    elif ay_no in [3, 4, 5]:
        mevsim = "İlkbahar"
    elif ay_no in [6, 7, 8]:
        mevsim = "Yaz"
    else:
        mevsim = "Sonbahar"
    
    print(f"{ay_no} -> {ay_ismi} -> {mevsim}")

else:

    print("Hata: Lütfen 1 ile 12 arasında bir sayı giriniz!")

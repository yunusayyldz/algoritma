# 1. Adım: Kullanıcıdan a sayısını alıyoruz
a = int(input("Bir sayı (a) giriniz: "))

# 2. Adım: Bölme işleminde 0 hatası olmasın diye kontrol ediyoruz
if a == 0:
    print("Hata: Bir sayı 0'a bölünemez!")
else:
    # --- Matematiksel Hile ---
    # 1/a işlemini yap, virgülü 3 basamak sağa kaydır (1000 ile çarp)
    # Sonra int() ile küsuratı tamamen at.
    deger = (1 / a) * 1000
    
    # Sadece tam kısmı alıyoruz
    ilk_uc_basamak = int(deger)
    
    print(f"1/{a} sayısının virgülden sonraki ilk 3 basamağı: {ilk_uc_basamak}")

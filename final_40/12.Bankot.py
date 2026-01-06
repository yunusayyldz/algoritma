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

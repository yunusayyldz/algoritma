print("Miras Hesaplama Programı")
print("Sorulara 1 (Evet) veya 0 (Hayır) olarak cevap veriniz.")

miras = 1.0

alt_soy = int(input("Ölenin alt soyu (çocuk/torun) var mı? (1/0): "))

if alt_soy == 1:
    es_var = int(input("Eş hayatta mı? (1/0): "))
    if es_var == 1:
        es_payi = 0.25
        print(f"Eşin Payı: {es_payi} (1/4)")
        kalan = miras - es_payi
    else:
        kalan = miras
    
    cocuk_sayisi = int(input("Çocuk sayısı: "))
    if cocuk_sayisi > 0:
        print(f"Çocuk başına düşen pay: {kalan / cocuk_sayisi}")

    else:
        ikinci_zumre = int(input("Anne, Baba veya Kardeş var mı? (1/0): "))
    
    if ikinci_zumre == 1:
        es_var = int(input("Eş hayatta mı? (1/0): "))
        if es_var == 1:
            es_payi = 0.50
            print(f"Eşin Payı: {es_payi} (1/2)")
            kalan = miras - es_payi
        else:
            kalan = miras
        
        anne_var = int(input("Anne sağ mı? (1/0): "))
        baba_var = int(input("Baba sağ mı? (1/0): "))
        
        dagitilacak_kardes_payi = 0
        
        if anne_var == 1:
            print(f"Anne Payı: {kalan / 2}")
        else:
            dagitilacak_kardes_payi += kalan / 2
            
        if baba_var == 1:
            print(f"Baba Payı: {kalan / 2}")
        else:
            dagitilacak_kardes_payi += kalan / 2
            
        if dagitilacak_kardes_payi > 0:
            kardes_sayisi = int(input("Kardeş sayısı: "))
            if kardes_sayisi > 0:
                print(f"Kardeş başına düşen pay: {dagitilacak_kardes_payi / kardes_sayisi}")

    else:
        ucuncu_zumre = int(input("Büyükanne veya Büyükbaba var mı? (1/0): "))
        
        if ucuncu_zumre == 1:
            es_var = int(input("Eş hayatta mı? (1/0): "))
            if es_var == 1:
                es_payi = 0.75
                print(f"Eşin Payı: {es_payi} (3/4)")
                kalan = miras - es_payi
            else:
                kalan = miras
            print(f"Büyükanne ve Büyükbaba tarafına düşen pay: {kalan}")
            
        else:
            es_var = int(input("Eş hayatta mı? (1/0): "))
            if es_var == 1:
                print(f"Eşin Payı: {miras} (Tamamı)")
            else:
                print("Miras Devlete Kalır.")

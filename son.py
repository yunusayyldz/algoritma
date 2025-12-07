def sor_1_0(soru):
    """
    Kullanıcıya soruyu sorar. 1 (Evet) veya 0 (Hayır) cevabını bekler.
    """
    while True:
        cevap = input(soru + " [1: Evet / 0: Hayır]: ").strip()
        
        if cevap == "1":
            return True
        elif cevap == "0":
            return False
        else:
            print("Hatalı giriş! Lütfen sadece 1 veya 0 tuşlayın.")

def sor_cocuk_sayisi():
    """
    Kullanıcıdan çocuk sayısını alır. Pozitif tam sayı bekler.
    """
    while True:
        try:
            sayi = int(input("Kaç çocuğu/torunu hayatta? (Sayi giriniz): ").strip())
            if sayi > 0:
                return sayi
            else:
                print("Hatalı giriş! Lütfen 1 veya daha büyük bir tam sayı girin.")
        except ValueError:
            print("Hatalı giriş! Lütfen bir tam sayı girin.")

def miras_hesapla():
    print("--- Miras Paylaşım Algoritması (Toplam Miras = 1) ---")
    print("Sorulara '1' (Evet) veya '0' (Hayır) yazarak cevap verin.\n")
    
    # Mirasın tamamı 1 birim olarak kabul ediliyor
    toplam_miras = 1.0
    
    # 1. ADIM: Eş durumu
    es_sag_mi = sor_1_0("Ölenin eşi sağ mı?")

    if es_sag_mi:
        # --- EŞ SAĞ ---
        
        # 1. Zümre (Çocuklar) kontrolü
        cocuk_var_mi = sor_1_0("Ölenin çocuğu veya torunu var mı?")
        
        if cocuk_var_mi:
            # Eş 1/4, Çocuklar 3/4
            cocuk_sayisi = sor_cocuk_sayisi() # <-- Çocuk sayısı burada soruluyor
            
            es_payi = 0.25
            cocuklarin_toplam_payi = 0.75
            her_cocuk_payi = cocuklarin_toplam_payi / cocuk_sayisi
            
            print("\nSONUÇ:")
            print(f"- Eş Payı: {es_payi}")
            print(f"- Çocukların Toplam Payı: {cocuklarin_toplam_payi}")
            print(f"- **Her Çocuğun Payı ({cocuk_sayisi} çocuk): {her_cocuk_payi:.4f}**")
        
        else:
            # Çocuk yoksa 2. Zümre (Anne/Baba)
            ikinci_zumre_var_mi = sor_1_0("Ölenin anne, baba veya kardeşi hayatta mı?")
            
            if ikinci_zumre_var_mi:
                # Eş 1/2, 2. Zümre 1/2
                es_payi = 0.50
                ikinci_zumre_payi = 0.50
                print("\nSONUÇ:")
                print(f"- Eş Payı: {es_payi}")
                print(f"- 2. Zümre Payı: {ikinci_zumre_payi}")
            
            else:
                # 2. Zümre yoksa 3. Zümre (Büyükler)
                ucuncu_zumre_var_mi = sor_1_0("Ölenin büyükanne veya büyükbabası hayatta mı?")
                
                if ucuncu_zumre_var_mi:
                    # Eş 3/4, 3. Zümre 1/4
                    es_payi = 0.75
                    ucuncu_zumre_payi = 0.25
                    print("\nSONUÇ:")
                    print(f"- Eş Payı: {es_payi}")
                    print(f"- 3. Zümre Payı: {ucuncu_zumre_payi}")
                else:
                    # Sadece Eş
                    es_payi = 1.0
                    print("\nSONUÇ:")
                    print(f"- Eş Payı: {es_payi}")

    else:
        # --- EŞ SAĞ DEĞİL ---
        
        cocuk_var_mi = sor_1_0("Ölenin çocuğu veya torunu var mı?")
        
        if cocuk_var_mi:
            cocuk_sayisi = sor_cocuk_sayisi() # <-- Çocuk sayısı burada da soruluyor
            
            her_cocuk_payi = toplam_miras / cocuk_sayisi
            
            print("\nSONUÇ:")
            print(f"- Çocukların Toplam Payı: {toplam_miras}")
            print(f"- **Her Çocuğun Payı ({cocuk_sayisi} çocuk): {her_cocuk_payi:.4f}**")
        
        else:
            ikinci_zumre_var_mi = sor_1_0("Ölenin anne, baba veya kardeşi hayatta mı?")
            
            if ikinci_zumre_var_mi:
                print("\nSONUÇ:")
                print(f"- 2. Zümre Payı: {toplam_miras}")
            
            else:
                ucuncu_zumre_var_mi = sor_1_0("Ölenin büyükanne veya büyükbabası hayatta mı?")
                
                if ucuncu_zumre_var_mi:
                    print("\nSONUÇ:")
                    print(f"- 3. Zümre Payı: {toplam_miras}")
                else:
                    print("\nSONUÇ:")
                    print(f"- Devlet Payı: {toplam_miras}")

# Programı başlat
if __name__ == "__main__":
    miras_hesapla()
# GRUP ÜYELERİ 
# KORAY AYAS
# YUNUS AYYILDIZ
# İSMAİL ÇAKIR

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

def sor_sayi(soru):
    """
    Kullanıcıdan pozitif tam sayı alır.
    """
    while True:
        try:
            sayi = int(input(soru + ": ").strip())
            if sayi > 0:
                return sayi
            else:
                print("Hatalı giriş! Lütfen 1 veya daha büyük bir tam sayı girin.")
        except ValueError:
            print("Hatalı giriş! Lütfen bir tam sayı girin.")

def miras_hesapla():
    print("="*60)
    print("MİRAS PAYLAŞIM ALGORITMASI")
    print("="*60)
    print("Toplam Miras = 1 birim (100%)")
    print("Sorulara '1' (Evet) veya '0' (Hayır) yazarak cevap verin.\n")
    
    toplam_miras = 1.0
    
    # ANA SORU: Eş var mı?
    es_var_mi = sor_1_0("Ölenin eşi sağ mı?")
    
    if es_var_mi:
        # ========== EŞ VAR ==========
        cocuk_var_mi = sor_1_0("Ölenin çocuğu var mı?")
        
        if cocuk_var_mi:
            # --- DURUM 1: EŞ VAR + ÇOCUK VAR ---
            cocuk_sayisi = sor_sayi("Kaç çocuğu var")
            
            cocuklardan_olen_var_mi = sor_1_0("Çocuklardan çocukları olup da ölen var mı?")
            
            if cocuklardan_olen_var_mi:
                olen_cocuk_sayisi = sor_sayi("Kaç tane çocuğu ölüp torunu var")
                
                # Eş 1/4, Çocuklar 3/4
                es_payi = 0.25
                cocuklarin_toplam_payi = 0.75
                her_cocuk_payi = cocuklarin_toplam_payi / cocuk_sayisi
                yasayan_cocuk = cocuk_sayisi - olen_cocuk_sayisi
                torunlara_toplam = her_cocuk_payi * olen_cocuk_sayisi
                
                print("\n" + "="*60)
                print("SONUÇ:")
                print("="*60)
                print(f"Eş: 1/4 = {es_payi} ({es_payi*100}%)")
                print(f"Çocukların Toplam Payı: 3/4 = {cocuklarin_toplam_payi} ({cocuklarin_toplam_payi*100}%)")
                print(f"- Yaşayan {yasayan_cocuk} çocuğun her birine: {her_cocuk_payi:.4f} ({her_cocuk_payi*100:.2f}%)")
                print(f"- Ölen {olen_cocuk_sayisi} çocuğun payı torunlarına: {torunlara_toplam:.4f} ({torunlara_toplam*100:.2f}%)")
                print(f"  (Her ölen çocuğun payı {her_cocuk_payi:.4f} kendi çocuklarına eşit bölünür)")
            else:
                # Ölü çocuk yok
                es_payi = 0.25
                cocuklarin_toplam_payi = 0.75
                her_cocuk_payi = cocuklarin_toplam_payi / cocuk_sayisi
                
                print("\n" + "="*60)
                print("SONUÇ:")
                print("="*60)
                print(f"Eş: 1/4 = {es_payi} ({es_payi*100}%)")
                print(f"Geri kalan {cocuk_sayisi} çocuğa eşit şekilde dağıtılır")
                print(f"Her çocuğa: {her_cocuk_payi:.4f} ({her_cocuk_payi*100:.2f}%)")
        
        else:
            # --- DURUM 2: EŞ VAR + ÇOCUK YOK ---
            # 2. Zümre kontrolü
            ikinci_zumre_var_mi = sor_1_0("2. Zümreden (Anne, Baba, Kardeş) hayatta olan var mı?")
            
            if ikinci_zumre_var_mi:
                anne_sag_mi = sor_1_0("Anne sağ mı?")
                baba_sag_mi = sor_1_0("Baba sağ mı?")
                kardesleri_var_mi = sor_1_0("Ölenin kardeşi sağ mı?")
                
                if kardesleri_var_mi:
                    # --- Alt Durum: Kardeş var ---
                    kardesi_kac = sor_sayi("Kaç kardeşi var")
                    
                    kardeslerden_olen_var_mi = sor_1_0("Kardeşlerden ölüp de çocuğu olan var mı?")
                    
                    if kardeslerden_olen_var_mi:
                        olen_kardes_sayisi = sor_sayi("Kaç tane kardeş ölüp çocuğu var")
                        
                        # Eş 1/4, Geri kalan 3/4 anne+baba+kardeşlere
                        es_payi = 0.25
                        geri_kalan = 0.75
                        
                        # Anne ve baba paylarını hesapla
                        toplam_kisi = 0
                        if anne_sag_mi:
                            toplam_kisi += 1
                        if baba_sag_mi:
                            toplam_kisi += 1
                        toplam_kisi += kardesi_kac
                        
                        her_kisi_payi = geri_kalan / toplam_kisi
                        yasayan_kardes = kardesi_kac - olen_kardes_sayisi
                        kardes_cocuklarina_toplam = her_kisi_payi * olen_kardes_sayisi
                        
                        print("\n" + "="*60)
                        print("SONUÇ:")
                        print("="*60)
                        print(f"Eş: 1/4 = {es_payi} ({es_payi*100}%)")
                        print(f"Geri kalan: 3/4 = {geri_kalan} ({geri_kalan*100}%)")
                        if anne_sag_mi:
                            print(f"- Anne: {her_kisi_payi:.4f} ({her_kisi_payi*100:.2f}%)")
                        if baba_sag_mi:
                            print(f"- Baba: {her_kisi_payi:.4f} ({her_kisi_payi*100:.2f}%)")
                        if yasayan_kardes > 0:
                            print(f"- Yaşayan {yasayan_kardes} kardeşin her birine: {her_kisi_payi:.4f} ({her_kisi_payi*100:.2f}%)")
                        print(f"- Ölen {olen_kardes_sayisi} kardeşin payı çocuklarına: {kardes_cocuklarina_toplam:.4f}")
                        print(f"  (Her ölen kardeşin payı {her_kisi_payi:.4f} kendi çocuklarına eşit bölünür)")
                    
                    else:
                        # Ölü kardeş yok
                        es_payi = 0.25
                        geri_kalan = 0.75
                        
                        toplam_kisi = 0
                        if anne_sag_mi:
                            toplam_kisi += 1
                        if baba_sag_mi:
                            toplam_kisi += 1
                        toplam_kisi += kardesi_kac
                        
                        her_kisi_payi = geri_kalan / toplam_kisi
                        
                        print("\n" + "="*60)
                        print("SONUÇ:")
                        print("="*60)
                        print(f"Eş: 1/4 = {es_payi} ({es_payi*100}%)")
                        print(f"Geri kalan kardeş sayısına bölünür: 3/4 = {geri_kalan} ({geri_kalan*100}%)")
                        if anne_sag_mi:
                            print(f"- Anne: {her_kisi_payi:.4f} ({her_kisi_payi*100:.2f}%)")
                        if baba_sag_mi:
                            print(f"- Baba: {her_kisi_payi:.4f} ({her_kisi_payi*100:.2f}%)")
                        print(f"- {kardesi_kac} kardeşin her birine: {her_kisi_payi:.4f} ({her_kisi_payi*100:.2f}%)")
                
                else:
                    # --- Alt Durum: Sadece Anne ve/veya Baba ---
                    es_payi = 0.50
                    geri_kalan = 0.50
                    
                    toplam_kisi = 0
                    if anne_sag_mi:
                        toplam_kisi += 1
                    if baba_sag_mi:
                        toplam_kisi += 1
                    
                    her_kisi_payi = geri_kalan / toplam_kisi if toplam_kisi > 0 else 0
                    
                    print("\n" + "="*60)
                    print("SONUÇ:")
                    print("="*60)
                    print(f"Eş: 2/4 = {es_payi} ({es_payi*100}%)")
                    print(f"Geriye kalan paylaştırılır: 2/4 = {geri_kalan} ({geri_kalan*100}%)")
                    if anne_sag_mi:
                        print(f"- Anne: {her_kisi_payi:.4f} ({her_kisi_payi*100:.2f}%)")
                    if baba_sag_mi:
                        print(f"- Baba: {her_kisi_payi:.4f} ({her_kisi_payi*100:.2f}%)")
            
            else:
                # --- DURUM 3: EŞ VAR + 2. Zümre YOK ---
                # 3. Zümre kontrolü
                ucuncu_zumre_var_mi = sor_1_0("3. Zümre (Büyükanne, Büyükbaba) hayatta mı?")
                
                if ucuncu_zumre_var_mi:
                    anneanne_sag_mi = sor_1_0("Anneanne sağ mı?")
                    dede_sag_mi = sor_1_0("Dede sağ mı?")
                    
                    es_payi = 0.75
                    ucuncu_zumre_payi = 0.25
                    
                    toplam_buyuk = 0
                    if anneanne_sag_mi:
                        toplam_buyuk += 1
                    if dede_sag_mi:
                        toplam_buyuk += 1
                    
                    her_buyuk_payi = ucuncu_zumre_payi / toplam_buyuk if toplam_buyuk > 0 else 0
                    
                    print("\n" + "="*60)
                    print("SONUÇ:")
                    print("="*60)
                    print(f"Eş: 3/4 = {es_payi} ({es_payi*100}%)")
                    print(f"3. Zümre: 1/4 = {ucuncu_zumre_payi} ({ucuncu_zumre_payi*100}%)")
                    if anneanne_sag_mi:
                        print(f"- Anneanne: {her_buyuk_payi:.4f} ({her_buyuk_payi*100:.2f}%)")
                    if dede_sag_mi:
                        print(f"- Dede: {her_buyuk_payi:.4f} ({her_buyuk_payi*100:.2f}%)")
                
                else:
                    # --- DURUM 4: Sadece Eş ---
                    es_payi = 1.0
                    print("\n" + "="*60)
                    print("SONUÇ:")
                    print("="*60)
                    print(f"Hepsi eşe kalır: {es_payi} ({es_payi*100}%)")
    
    else:
        # ========== EŞ YOK ==========
        cocuk_var_mi = sor_1_0("Ölenin çocuğu var mı?")
        
        if cocuk_var_mi:
            # --- DURUM 5: EŞ YOK + ÇOCUK VAR ---
            cocuk_sayisi = sor_sayi("Kaç çocuğu var")
            
            cocuklardan_olen_var_mi = sor_1_0("Çocuklardan çocukları olup da ölen var mı?")
            
            if cocuklardan_olen_var_mi:
                olen_cocuk_sayisi = sor_sayi("Kaç tane çocuğu ölüp torunu var")
                
                her_cocuk_payi = toplam_miras / cocuk_sayisi
                yasayan_cocuk = cocuk_sayisi - olen_cocuk_sayisi
                torunlara_toplam = her_cocuk_payi * olen_cocuk_sayisi
                
                print("\n" + "="*60)
                print("SONUÇ:")
                print("="*60)
                print(f"Miras çocuklara eşit şekilde dağıtılır")
                print(f"- Yaşayan {yasayan_cocuk} çocuğun her birine: {her_cocuk_payi:.4f} ({her_cocuk_payi*100:.2f}%)")
                print(f"- Ölen {olen_cocuk_sayisi} çocuğun payı torunlarına: {torunlara_toplam:.4f} ({torunlara_toplam*100:.2f}%)")
                print(f"  (Her ölen çocuğun payı {her_cocuk_payi:.4f} kendi çocuklarına eşit bölünür)")
            
            else:
                her_cocuk_payi = toplam_miras / cocuk_sayisi
                
                print("\n" + "="*60)
                print("SONUÇ:")
                print("="*60)
                print(f"Miras {cocuk_sayisi} çocuğa eşit şekilde dağıtılır")
                print(f"Her çocuğa: {her_cocuk_payi:.4f} ({her_cocuk_payi*100:.2f}%)")
        
        else:
            # --- DURUM 6: EŞ YOK + ÇOCUK YOK ---
            # 2. Zümre kontrolü
            ikinci_zumre_var_mi = sor_1_0("2. Zümreden (Anne, Baba, Kardeş) hayatta olan var mı?")
            
            if ikinci_zumre_var_mi:
                anne_sag_mi = sor_1_0("Anne sağ mı?")
                baba_sag_mi = sor_1_0("Baba sağ mı?")
                kardesleri_var_mi = sor_1_0("Kardeş sağ mı?")
                
                if kardesleri_var_mi:
                    kardesi_kac = sor_sayi("Kaç kardeşi var")
                    
                    kardeslerden_olen_var_mi = sor_1_0("Kardeşlerden ölüp de çocuğu olan var mı?")
                    
                    if kardeslerden_olen_var_mi:
                        olen_kardes_sayisi = sor_sayi("Kaç tane kardeş ölüp çocuğu var")
                        
                        toplam_kisi = 0
                        if anne_sag_mi:
                            toplam_kisi += 1
                        if baba_sag_mi:
                            toplam_kisi += 1
                        toplam_kisi += kardesi_kac
                        
                        her_kisi_payi = toplam_miras / toplam_kisi
                        yasayan_kardes = kardesi_kac - olen_kardes_sayisi
                        kardes_cocuklarina_toplam = her_kisi_payi * olen_kardes_sayisi
                        
                        print("\n" + "="*60)
                        print("SONUÇ:")
                        print("="*60)
                        print(f"Miras 2. zümreye paylaştırılır")
                        if anne_sag_mi:
                            print(f"- Anne: {her_kisi_payi:.4f} ({her_kisi_payi*100:.2f}%)")
                        if baba_sag_mi:
                            print(f"- Baba: {her_kisi_payi:.4f} ({her_kisi_payi*100:.2f}%)")
                        if yasayan_kardes > 0:
                            print(f"- Yaşayan {yasayan_kardes} kardeşin her birine: {her_kisi_payi:.4f} ({her_kisi_payi*100:.2f}%)")
                        print(f"- Ölen {olen_kardes_sayisi} kardeşin payı çocuklarına: {kardes_cocuklarina_toplam:.4f}")
                        print(f"  (Her ölen kardeşin payı {her_kisi_payi:.4f} kendi çocuklarına eşit bölünür)")
                    
                    else:
                        toplam_kisi = 0
                        if anne_sag_mi:
                            toplam_kisi += 1
                        if baba_sag_mi:
                            toplam_kisi += 1
                        toplam_kisi += kardesi_kac
                        
                        her_kisi_payi = toplam_miras / toplam_kisi
                        
                        print("\n" + "="*60)
                        print("SONUÇ:")
                        print("="*60)
                        print(f"Miras 2. zümreye paylaştırılır")
                        if anne_sag_mi:
                            print(f"- Anne: {her_kisi_payi:.4f} ({her_kisi_payi*100:.2f}%)")
                        if baba_sag_mi:
                            print(f"- Baba: {her_kisi_payi:.4f} ({her_kisi_payi*100:.2f}%)")
                        print(f"- {kardesi_kac} kardeşin her birine: {her_kisi_payi:.4f} ({her_kisi_payi*100:.2f}%)")
                
                else:
                    # Sadece anne ve/veya baba
                    toplam_kisi = 0
                    if anne_sag_mi:
                        toplam_kisi += 1
                    if baba_sag_mi:
                        toplam_kisi += 1
                    
                    her_kisi_payi = toplam_miras / toplam_kisi if toplam_kisi > 0 else 0
                    
                    print("\n" + "="*60)
                    print("SONUÇ:")
                    print("="*60)
                    print(f"Miras 2. zümreye paylaştırılır")
                    if anne_sag_mi:
                        print(f"- Anne: {her_kisi_payi:.4f} ({her_kisi_payi*100:.2f}%)")
                    if baba_sag_mi:
                        print(f"- Baba: {her_kisi_payi:.4f} ({her_kisi_payi*100:.2f}%)")
            
            else:
                # --- DURUM 7: EŞ YOK + 2. Zümre YOK ---
                # 3. Zümre kontrolü
                ucuncu_zumre_var_mi = sor_1_0("3. Zümre hayatta mı?")
                
                if ucuncu_zumre_var_mi:
                    anneanne_sag_mi = sor_1_0("Anneanne sağ mı?")
                    dede_sag_mi = sor_1_0("Dede sağ mı?")
                    
                    toplam_buyuk = 0
                    if anneanne_sag_mi:
                        toplam_buyuk += 1
                    if dede_sag_mi:
                        toplam_buyuk += 1
                    
                    her_buyuk_payi = toplam_miras / toplam_buyuk if toplam_buyuk > 0 else 0
                    
                    print("\n" + "="*60)
                    print("SONUÇ:")
                    print("="*60)
                    print(f"Miras 3. zümreye paylaştırılır")
                    if anneanne_sag_mi:
                        print(f"- Anneanne: {her_buyuk_payi:.4f} ({her_buyuk_payi*100:.2f}%)")
                    if dede_sag_mi:
                        print(f"- Dede: {her_buyuk_payi:.4f} ({her_buyuk_payi*100:.2f}%)")
                
                else:
                    # --- DURUM 8: Miras devlete kalır ---
                    print("\n" + "="*60)
                    print("SONUÇ:")
                    print("="*60)
                    print(f"Miras devlete kalır: {toplam_miras} ({toplam_miras*100}%)")
    
    print("="*60)

# Programı başlat
if __name__ == "__main__":
    miras_hesapla()
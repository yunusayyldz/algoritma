def metin_analizi(metin):
    # Sayaçlarımızı sıfırdan başlatıyoruz
    harf_sayisi = 0
    rakam_sayisi = 0
    bosluk_sayisi = 0
    ozel_karakter_sayisi = 0
    
    for karakter in metin:
        
        # 1. Kontrol: Harf mi? (a-z, A-Z ve Türkçe karakterler)
        if karakter.isalpha():
            harf_sayisi += 1
            
        # 2. Kontrol: Rakam mı? (0-9)
        elif karakter.isdigit():
            rakam_sayisi += 1
            
        # 3. Kontrol: Boşluk mu? (Space tuşu, Tab vb.)
        elif karakter.isspace():
            bosluk_sayisi += 1
            
        # 4. Kontrol: Hiçbiri değilse Özel Karakterdir (., !, @, #, $, % vb.)
        else:
            ozel_karakter_sayisi += 1

    # Sonuçları Yazdır
    print("-" * 30)
    print("📊 METİN ANALİZ RAPORU")
    print("-" * 30)
    print(f"Metin Uzunluğu       : {len(metin)}")
    print(f"🅰️  Harf Sayısı       : {harf_sayisi}")
    print(f"🔢 Rakam Sayısı      : {rakam_sayisi}")
    print(f"⬜ Boşluk Sayısı     : {bosluk_sayisi}")
    print(f"🔣 Özel Karakter     : {ozel_karakter_sayisi}")

# --- Ana Program ---
girilen_metin = input("Lütfen analiz edilecek metni giriniz: ")

metin_analizi(girilen_metin)

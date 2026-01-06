def sezar_sifre(metin, anahtar, islem_turu='sifrele'):
    sonuc = ""
    
    # Eğer işlem çözme ise, anahtarı negatife çeviririz.
    # Yani 3 ileri gitmek yerine 3 geri gideriz.
    if islem_turu == 'coz':
        anahtar = -anahtar
        
    for karakter in metin:
        # Sadece harfleri değiştir, boşluk veya noktaya dokunma
        if karakter.isalpha():
            
            # Büyük harf mi küçük harf mi?
            # ASCII tablosunda 'A' 65, 'a' 97'den başlar.
            baslangic = 65 if karakter.isupper() else 97
            
            # --- Matematiksel Formül ---
            # 1. (ord - baslangic): Harfi 0-25 arasına indir (A=0, B=1...)
            # 2. (+ anahtar): Kaydırma işlemini yap
            # 3. (% 26): 'z'den sonra başa dönmesi için mod al
            yeni_kod = (ord(karakter) - baslangic + anahtar) % 26 + baslangic
            
            sonuc += chr(yeni_kod)
        else:
            # Harf değilse (boşluk, ünlem vs.) olduğu gibi ekle
            sonuc += karakter
            
    return sonuc

# --- Ana Program ---
print("--- Sezar Şifreleme Programı ---")
girilen_metin = input("Metni giriniz: ")
kaydirma_miktari = int(input("Anahtar sayısı (Kaç harf kaysın?): "))

# 1. Şifreleme
sifreli_hal = sezar_sifre(girilen_metin, kaydirma_miktari, 'sifrele')
print(f"\n🔒 Şifreli Metin: {sifreli_hal}")

# 2. Çözme (Sağlama yapalım)
cozulmus_hal = sezar_sifre(sifreli_hal, kaydirma_miktari, 'coz')
print(f"🔓 Çözülmüş Metin: {cozulmus_hal}")

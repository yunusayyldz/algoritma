def frekans_hesapla(metin):
    # 1. Adım: Metni temizle ve küçük harfe çevir
    metin = metin.lower()
    
    # Noktalama işaretlerini boşlukla değiştirelim veya silelim
    noktalama_isaretleri = ".,!?;:()-"
    for isaret in noktalama_isaretleri:
        metin = metin.replace(isaret, "")
    
    # 2. Adım: Kelimelere ayır
    kelimeler = metin.split()
    
    # Sonuçları tutacak boş bir sözlük (dictionary)
    frekans_sozlugu = {}
    
    # 3. Adım: Her kelimeyi say
    for kelime in kelimeler:
        if kelime in frekans_sozlugu:
            # Kelime zaten listede varsa, sayısını 1 artır
            frekans_sozlugu[kelime] += 1
        else:
            # Kelime ilk defa görüldüyse, listeye 1 olarak ekle
            frekans_sozlugu[kelime] = 1
            
    return frekans_sozlugu

# --- Ana Program ---
girdi_metni = input("Bir metin giriniz: ")

sonuc = frekans_hesapla(girdi_metni)

print("\n--- Kelime Frekansları ---")
# Sözlükteki verileri (anahtar, deger) şeklinde döngüye sokuyoruz
for kelime, sayi in sonuc.items():
    print(f"'{kelime}': {sayi} kez")

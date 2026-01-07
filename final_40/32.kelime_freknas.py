def frekans_hesapla(metin):

    metin = metin.lower()
    
    noktalama_isaretleri = ".,!?;:()-"
    for isaret in noktalama_isaretleri:
        metin = metin.replace(isaret, "")
    
    kelimeler = metin.split()

    frekans_sozlugu = {}
    
    for kelime in kelimeler:
        if kelime in frekans_sozlugu:

            frekans_sozlugu[kelime] += 1
        else:

            frekans_sozlugu[kelime] = 1
            
    return frekans_sozlugu

girdi_metni = input("Bir metin giriniz: ")

sonuc = frekans_hesapla(girdi_metni)

print("\n--- Kelime Frekansları ---")

for kelime, sayi in sonuc.items():
    print(f"'{kelime}': {sayi} kez")

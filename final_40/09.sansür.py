# 1. Adım: Cümleyi alıyoruz
metin = input("Lütfen bir cümle giriniz: ")

# 2. Adım: Cümleyi kelimelere ayırıyoruz (Liste haline getiriyoruz)
# "Merhaba Dünya" -> ["Merhaba", "Dünya"] olur.
kelimeler = metin.split()

# İşlenmiş yeni kelimeleri biriktireceğimiz boş bir liste
yeni_kelime_listesi = []

# 3. Adım: Her kelimeyi sırayla işliyoruz
for kelime in kelimeler:
    # Kelimenin sadece ilk harfini al
    ilk_harf = kelime[0]
    
    # Geriye kalan harf sayısı kadar yıldız oluştur
    # (Kelime uzunluğu - 1) bize kaç yıldız gerektiğini söyler.
    yildizlar = "*" * (len(kelime) - 1)
    
    # İlk harf ile yıldızları birleştir
    maskeli_kelime = ilk_harf + yildizlar
    
    # Bu yeni hali listemize ekle
    yeni_kelime_listesi.append(maskeli_kelime)

# 4. Adım: Kelimeleri tekrar birleştirip cümle yapıyoruz
# " ".join(...) komutu, listedeki parçaları aralarına boşluk koyarak birleştirir.
sonuc = " ".join(yeni_kelime_listesi)

print("Sonuç:", sonuc)

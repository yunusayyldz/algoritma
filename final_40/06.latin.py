# 1. Adım: Çeviri tablomuzu (Sözlük) oluşturuyoruz
# Sol taraftakiler Türkçe, sağ taraftakiler Latin karşılıklarıdır.
ceviri_tablosu = {
    "ç": "c", "Ç": "C",
    "ğ": "g", "Ğ": "G",
    "ı": "i", "İ": "I",
    "ö": "o", "Ö": "O",
    "ş": "s", "Ş": "S",
    "ü": "u", "Ü": "U"
}

# 2. Adım: Kullanıcıdan metni alıyoruz
metin = input("Lütfen Türkçe karakter içeren bir metin giriniz: ")

# 3. Adım: Tablodaki her harfi tek tek kontrol edip değiştiriyoruz
# Bu döngü, sözlüğün içindeki her ikiliyi (turkce, latin) sırayla alır.
for turkce, latin in ceviri_tablosu.items():
    # Metnin içindeki Türkçe harfi bulur ve Latin haliyle değiştirir.
    metin = metin.replace(turkce, latin)

# 4. Adım: Sonucu ekrana yazdırıyoruz
print("Dönüştürülmüş hali:", metin)

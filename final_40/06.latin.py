ceviri_tablosu = {
    "ç": "c", "Ç": "C",
    "ğ": "g", "Ğ": "G",
    "ı": "i", "İ": "I",
    "ö": "o", "Ö": "O",
    "ş": "s", "Ş": "S",
    "ü": "u", "Ü": "U"
}

metin = input("Lütfen Türkçe karakter içeren bir metin giriniz: ")

for turkce, latin in ceviri_tablosu.items():
    
    metin = metin.replace(turkce, latin)

print("Dönüştürülmüş hali:", metin)

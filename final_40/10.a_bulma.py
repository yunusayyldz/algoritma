# 1. Adım: Kullanıcıdan cümleyi alıyoruz
# .lower() ekledik ki büyük 'A' içeren kelimeleri de (örneğin 'Ankara') kaçırmayalım.
metin = input("Lütfen bir cümle giriniz: ").lower()

# 2. Adım: Cümleyi kelimelere ayırıyoruz
kelimeler = metin.split()

# Sayacımızı sıfırlıyoruz
sayac = 0

# 3. Adım: Kelimeleri tek tek kontrol ediyoruz
for kelime in kelimeler:
    # Python'da "in" kelimesi "içinde var mı?" sorusunu sorar.
    if "a" in kelime:
        sayac += 1  # Varsa sayacı artır

# 4. Adım: Sonucu yazdırıyoruz
print(f"İçinde 'a' harfi geçen kelime sayısı: {sayac}")

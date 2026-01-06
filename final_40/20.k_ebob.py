def en_buyuk_boleni_bul(sayi):
    # 1. Adım: Özel durum kontrolü
    if sayi <= 1:
        return "1'den büyük bir sayı girilmelidir."

    # 2. Adım: Aramaya sayının yarısından başlıyoruz.
    # (Tam bölme '//' yaparak küsuratla uğraşmıyoruz)
    baslangic = sayi // 2
    
    # 3. Adım: Geriye doğru (1'e kadar) sayıyoruz
    # range(başlangıç, bitiş, adım) -> (yarısı, 0, -1)
    for i in range(baslangic, 0, -1):
        
        # Eğer tam bölünüyorsa, bulduğumuz ilk sayı EN BÜYÜK olandır.
        if sayi % i == 0:
            return i

# --- Test Edelim ---
girdi = int(input("Bir sayı giriniz: "))

sonuc = en_buyuk_boleni_bul(girdi)

print(f"{girdi} sayısının kendisi hariç en büyük böleni: {sonuc}")

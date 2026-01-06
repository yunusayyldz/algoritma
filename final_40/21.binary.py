#2 lik sayı sistemine göre
def binarye_cevir(sayi):
    # Özel Durum: Sayı 0 ise direkt "0" döndür
    if sayi == 0:
        return "0"
    
    # Sonucu biriktireceğimiz boş bir metin (string)
    binary_karsilik = ""
    
    while sayi > 0:
        kalan = sayi % 2      # 2'ye bölümünden kalanı bul (0 veya 1)
        
        # DİKKAT: Kalanı mevcut sonucun BAŞINA ekliyoruz.
        # Çünkü binary sistemde son kalan en başa yazılır.
        binary_karsilik = str(kalan) + binary_karsilik
        
        sayi = sayi // 2      # Sayıyı ikiye bölüp küçültüyoruz
        
    return binary_karsilik

# --- Test Edelim ---
girilen_sayi = int(input("Bir sayı giriniz: "))

sonuc = binarye_cevir(girilen_sayi)

print(f"{girilen_sayi} sayısının Binary (2'lik) karşılığı: {sonuc}")

def mukemmel_sayi_kontrol(sayi):
    # Negatif sayılar ve 1 mükemmel sayı değildir
    if sayi < 2:
        return False
        
    toplam = 0
    
    # Optimizasyon: Sayının yarısına kadar gitmek yeterlidir.
    # range fonksiyonunda son sayı dahil olmadığı için +1 ekliyoruz.
    limit = (sayi // 2) + 1
    
    for i in range(1, limit):
        # Eğer tam bölünüyorsa toplama ekle
        if sayi % i == 0:
            toplam += i
            
    # Döngü bittiğinde kontrol et
    if toplam == sayi:
        return True
    else:
        return False

# --- Ana Program ---
girdi = int(input("Bir sayı giriniz: "))

if mukemmel_sayi_kontrol(girdi):
    print(f"✅ TEBRİKLER! {girdi} bir Mükemmel Sayıdır.")
else:
    print(f"❌ {girdi} mükemmel sayı değildir.")

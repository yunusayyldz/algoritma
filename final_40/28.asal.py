def asal_mi(sayi):
    # 1. Kural: 1 ve negatif sayılar asal değildir.
    if sayi <= 1:
        return False
    
    # 2. Kural: 2 tek çift asal sayıdır.
    if sayi == 2:
        return True
    
    # 3. Kural: Döngü Sınırı (Optimizasyon)
    # Sayının kareköküne kadar gitmek yeterlidir.
    # int(sayi ** 0.5) karekök alır. +1 ekliyoruz ki sınır dahil olsun.
    limit = int(sayi ** 0.5) + 1
    
    # 2'den başlayıp limite kadar dönüyoruz
    for i in range(2, limit):
        if sayi % i == 0:
            return False  # Bölen bulundu! Asal değil.
            
    return True  # Döngü bitti ve hiç bölen çıkmadıysa asaldır.

# --- Test Edelim ---
girdi = int(input("Kontrol edilecek sayıyı giriniz: "))

if asal_mi(girdi):
    print(f"{girdi} bir ASAL sayıdır.")
else:
    print(f"{girdi} asal değildir.")

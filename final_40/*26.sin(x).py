import math  # Faktöriyel ve Pi sayısı için gerekli

# 1. Adım: Kullanıcıdan açıyı alıyoruz
derece = float(input("Açıyı giriniz (Derece cinsinden, örn: 30): "))

# 2. Adım: Dereceyi Radyana çeviriyoruz
# Matematiksel serilerde her zaman Radyan kullanılır.
# Formül: Radyan = Derece * (Pi / 180)
x = derece * (math.pi / 180)

toplam = 0
isaret = 1  # İlk terim pozitif (+) başlar

print(f"\n--- Hesaplama Adımları (x = {x:.4f} radyan) ---")

# 3. Adım: 1'den 9'a kadar (10 hariç) 2'şer atlayarak döngü kuruyoruz
# n değerleri sırasıyla: 1, 3, 5, 7, 9 olacak.
for n in range(1, 10, 2):
    
    # Formül: (x üzeri n) / (n faktöriyel)
    ust_kisim = x ** n
    alt_kisim = math.factorial(n)
    
    terim = (ust_kisim / alt_kisim) * isaret
    
    # Hesaplanan terimi toplama ekle
    toplam += terim
    
    # Adımları görmek için yazdıralım (İsteğe bağlı)
    print(f"Derece {n}. Terim: {terim:.6f}")
    
    # Bir sonraki tur için işareti tersine çevir (+ ise -, - ise + yap)
    isaret = -isaret

# 4. Adım: Sonuçları karşılaştırıyoruz
print("-" * 30)
print(f"Maclaurin ile hesaplanan: {toplam:.8f}")
print(f"Python'un kendi math.sin fonksiyonu: {math.sin(x):.8f}")

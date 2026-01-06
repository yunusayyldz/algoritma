import math  # Matematiksel işlemler için gerekli kütüphane

# 1. Adım: Değerleri kullanıcıdan alıyoruz
# Kenarlar ve açı ondalıklı (float) olabilir.
a = float(input("Birinci kenar uzunluğunu (a) giriniz: "))
b = float(input("İkinci kenar uzunluğunu (b) giriniz: "))
aci = float(input("Aradaki açıyı (derece olarak) giriniz: "))

# 2. Adım: Formülü uyguluyoruz
# math.sin -> Sinüs hesaplar
# math.pi  -> Pi sayısını (3.14159...) getirir
alan = a * b * math.sin(aci * math.pi / 180) / 2

# 3. Adım: Sonucu biraz sadeleştirerek yazdırıyoruz
# .2f ifadesi virgülden sonra sadece 2 basamak göster demektir.
print(f"Üçgenin Alanı: {alan:.2f}")

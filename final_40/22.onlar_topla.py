genel_toplam = 0

print("--- 10 Adet Sayı Giriniz ---")

for i in range(1, 11):
    girilen_sayi = int(input(f"{i}. sayıyı giriniz: "))

    rakam = (girilen_sayi // 10) % 10
    
    basamak_degeri = rakam * 10
    
    genel_toplam += basamak_degeri

print("-" * 30)
print(f"Onlar basamağındaki değerlerin toplamı: {genel_toplam}")

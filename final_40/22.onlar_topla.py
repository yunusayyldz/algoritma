# Toplamı tutacak değişken
genel_toplam = 0

print("--- 10 Adet Sayı Giriniz ---")

# 10 kez dönecek döngü
for i in range(1, 11):
    girilen_sayi = int(input(f"{i}. sayıyı giriniz: "))
    
    # 1. Adım: Onlar basamağındaki RAKAMI bul
    # (Sayıyı 10'a böl, son basamağı al)
    rakam = (girilen_sayi // 10) % 10
    
    # 2. Adım: Bu rakamın BASAMAK DEĞERİNİ bul (10 ile çarp)
    basamak_degeri = rakam * 10
    
    # 3. Adım: Toplama ekle
    genel_toplam += basamak_degeri
    
    # İstersen her adımda ne eklediğini görebilirsin (Opsiyonel)
    # print(f"-> {girilen_sayi} için eklenen değer: {basamak_degeri}")

print("-" * 30)
print(f"Onlar basamağındaki değerlerin toplamı: {genel_toplam}")

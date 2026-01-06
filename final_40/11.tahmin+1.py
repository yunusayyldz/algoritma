import random  # Rastgele sayı üretmek için gerekli kütüphane

puan = 0  # Başlangıç puanımız

print("--- Sayı Tahmin Oyunu Başladı! ---")
print("Hedef: 5 puan toplamak.\n")

# Puan 5'ten küçük olduğu sürece bu döngü dönmeye devam eder.
while puan < 5:
    # 1. Adım: Bilgisayar 1-5 arası sayı tutar
    gizli_sayi = random.randint(1, 5)
    
    # 2. Adım: Kullanıcıdan tahmin istenir
    # input'u int() ile tam sayıya çeviriyoruz.
    tahmin = int(input(f"Puanın {puan}. Tahminin (1-5 arası): "))
    
    # 3. Adım: Kontrol
    if tahmin == gizli_sayi:
        puan += 1  # Puanı 1 artır
        print("Tebrikler! Doğru bildin.")
    else:
        print(f"Maalesef... Tuttuğum sayı {gizli_sayi} idi.")
    
    print("-" * 20)  # Görsel olarak turları ayırmak için çizgi

# Döngü bittiğinde burası çalışır
print("\nOyun Bitti! Toplam 5 puana ulaştın, şampiyonsun!")

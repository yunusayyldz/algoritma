import random

def oyunu_baslat():
    print("--- 4 Basamaklı Sayı Bulmaca Oyunu ---")
    print("Kural: Rakamları farklı 4 basamaklı bir sayı tuttum.")
    print("İpuçları:\n (+) -> Rakam ve yeri doğru.\n (-) -> Rakam doğru ama yeri yanlış.\n")

    # 1. ADIM: Bilgisayarın sayıyı üretmesi
    # Rakamları farklı olması için random.sample kullanıyoruz.
    # İlk basamak 0 olmasın diye kontrol ediyoruz.
    while True:
        rakamlar = random.sample(range(10), 4) # Örn: [0, 4, 2, 9]
        if rakamlar[0] != 0:
            # Listeyi string'e çeviriyoruz (Örn: "4029")
            gizli_sayi = "".join(map(str, rakamlar))
            break

    tahmin_sayisi = 0

    # 2. ADIM: Oyun Döngüsü
    while True:
        tahmin = input("Tahmininiz (4 basamaklı): ")

        # Hatalı giriş kontrolü (Uzunluk ve sayı olma durumu)
        if len(tahmin) != 4 or not tahmin.isdigit():
            print("Lütfen 4 haneli bir sayı giriniz!")
            continue # Döngünün başına dön
            
        # Rakamları farklı mı kontrolü (Opsiyonel ama iyi bir kuraldır)
        if len(set(tahmin)) != 4:
            print("Lütfen rakamları birbirinden farklı bir sayı giriniz!")
            continue

        tahmin_sayisi += 1
        arti_sayisi = 0
        eksi_sayisi = 0

        # 3. ADIM: Karşılaştırma Mantığı
        for i in range(4):
            # O anki rakam bilgisayarın sayısında hiç var mı?
            if tahmin[i] in gizli_sayi:
                # Varsa, yeri de aynı mı?
                if tahmin[i] == gizli_sayi[i]:
                    arti_sayisi += 1
                else:
                    eksi_sayisi += 1
        
        # Sonucu yazdır
        print(f"Sonuç: +{arti_sayisi} , -{eksi_sayisi}")

        # 4. ADIM: Kazanma Kontrolü
        if arti_sayisi == 4:
            print("-" * 30)
            print(f"TEBRİKLER! Sayıyı {tahmin_sayisi}. denemede buldunuz.")
            break # Oyunu bitir

# Oyunu çalıştır
oyunu_baslat()

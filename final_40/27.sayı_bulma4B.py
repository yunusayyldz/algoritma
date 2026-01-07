import random

def oyunu_baslat():
    print("--- 4 Basamaklı Sayı Bulmaca Oyunu ---")
    print("Kural: Rakamları farklı 4 basamaklı bir sayı tuttum.")
    print("İpuçları:\n (+) -> Rakam ve yeri doğru.\n (-) -> Rakam doğru ama yeri yanlış.\n")


    while True:
        rakamlar = random.sample(range(10), 4) 
        if rakamlar[0] != 0:

            gizli_sayi = "".join(map(str, rakamlar))
            break

    tahmin_sayisi = 0

    while True:
        tahmin = input("Tahmininiz (4 basamaklı): ")

        if len(tahmin) != 4 or not tahmin.isdigit():
            print("Lütfen 4 haneli bir sayı giriniz!")
            continue

        if len(set(tahmin)) != 4:
            print("Lütfen rakamları birbirinden farklı bir sayı giriniz!")
            continue

        tahmin_sayisi += 1
        arti_sayisi = 0
        eksi_sayisi = 0


        for i in range(4):

            if tahmin[i] in gizli_sayi:

                if tahmin[i] == gizli_sayi[i]:
                    arti_sayisi += 1
                else:
                    eksi_sayisi += 1
        
        print(f"Sonuç: +{arti_sayisi} , -{eksi_sayisi}")

        if arti_sayisi == 4:
            print("-" * 30)
            print(f"TEBRİKLER! Sayıyı {tahmin_sayisi}. denemede buldunuz.")
            break 

oyunu_baslat()

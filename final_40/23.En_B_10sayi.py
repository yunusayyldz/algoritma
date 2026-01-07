print("--- En Büyük Sayıyı Bulma Programı ---")

en_buyuk = int(input("1. sayıyı giriniz: "))

for i in range(2, 11):
    sayi = int(input(f"{i}. sayıyı giriniz: "))
    
    if sayi > en_buyuk:
        en_buyuk = sayi 

print("-" * 30)
print(f"Girdiğiniz sayılar içinde en büyüğü: {en_buyuk}")

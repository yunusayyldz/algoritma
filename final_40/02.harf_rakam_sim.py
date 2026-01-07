veri = input("Lütfen klavyeden bir tuşa basınız (Tek karakter): ")

if veri.isalpha():
    print("Girdiğiniz karakter bir HARF'tir.")

elif veri.isdigit():
    print("Girdiğiniz karakter bir RAKAM'dır.")

else:
    print("Girdiğiniz karakter bir SİMGE'dir.")

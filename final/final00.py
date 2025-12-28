def roma(num):
    sonuc = ""
    while num >= 50: 
        sonuc += "L"
        num -= 50
    if num >= 40 :
        sonuc += "XL"
        num -= 40
    while num >= 10 :
        sonuc += "X"
        num -= 10
    if num >= 9 :
        sonuc += "IX"
        num -= 9
    while num >= 5 :
        sonuc += "V"
        num -= 5
    if num >= 4 :
        sonuc += "IV"
        num -= 4
    while num >= 1 :
        sonuc += "I"
    return sonuc
sayi = int(input("değiştirilmesini istediğiniz sayıyı giriniz"))
print("roma rakamlı hali şu şekil:",roma(sayi))

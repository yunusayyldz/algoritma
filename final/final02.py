def toplama(num1,num2):
    return num1 + num2

def cıkarma(num1,num2):
    return num1 - num2

def bolme(num1,num2):
    return num1 / num2

def carpma(num1,num2):
    return num1 * num2

while True :
    sayi1 = int(input("1.sayıyı giriniz:"))
    sayi2 = int(input("2.sayıyı giriniz:"))
    sayi = int(input("\n toplama için 1 \n çıkarma için 2 \n bölme için 3 \n çarpma için 4 \n \n ! çıkmak için 0 ! \n \n giriniz:"))

    if sayi == 1 :
        print("sonuç :",toplama(sayi1,sayi2))
    elif sayi == 2 :
        print("sonuç:",cıkarma(sayi1,sayi2))
    elif sayi == 3 :
        print("sonuç:",bolme(sayi1,sayi2))
    elif sayi == 4 :
        print("sonuç:",carpma(sayi1,sayi2))
    elif sayi == 0 :
        print("bitti")
        break
    else:
        print("geçerli sayı giriniz !")

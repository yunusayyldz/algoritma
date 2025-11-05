num=int(input("sayı:"))

while num<5:
    
    print("sayı giriniz",num)
    sayi=int(input("sayi:"))
    print("en son girdiğiniz sayı doğru")
    

while True:
    num=int(input("sayı giriniz:"))
    if num > 5:
        print("doğru sayıyı girdiniz")
        break
#not: while ture dersek içindekini haberi dönderir taki altında döngüden çıkmasını sağlıyacak if veya başka bir şey girene kadar
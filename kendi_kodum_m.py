print("miras hesaplama programına hoş geldiniz öncelikle başınız sağolsun")

print("evet = 1, hayır = 0 olacak şekilde cevaplayınız")

es = int(input("ölenin eşi hayata mı  1/0 :"))
bebek = int(input("ölenin alt soyundan sağ olan var mı:"))
miras = 1.0
if es == 1 :
    kalan = miras / 4
    print(f"eşin payı : {kalan}")
    if bebek == 1 :
        gariplere = miras - kalan
        adet = int(input("çocuk sayısı: "))
        match adet :
            case 1:
                num1 = int(input("1.çocuk sağ mı ölümü : "))
                toplam = num1 
                
                kişib = gariplere / toplam
                print(f"çocukların kişi başına düşen payı : {kişib}")        
        
            case 2:
                num1 = int(input("1.çocuk sağ mı ölümü : "))
                num2 = int(input("1.çocuk sağ mı ölümü : "))
                toplam = num1 + num2 
                
                kişib = gariplere / toplam
                print(f"çocukların kişi başına düşen payı : {kişib}")        
        
            case 3:
                num1 = int(input("1.çocuk sağ mı ölümü : "))
                num2 = int(input("1.çocuk sağ mı ölümü : "))
                num3 = int(input("1.çocuk sağ mı ölümü : "))
                toplam = num1 + num2 + num3
                
                kişib = gariplere / toplam
                print(f"çocukların kişi başına düşen payı : {kişib}")        
        
            case 4:
                num1 = int(input("1.çocuk sağ mı ölümü : "))
                num2 = int(input("1.çocuk sağ mı ölümü : "))
                num3 = int(input("1.çocuk sağ mı ölümü : "))
                num4 = int(input("1.çocuk sağ mı ölümü : "))
                toplam = num1 + num2 + num3 + num4
                
                kişib = gariplere / toplam
                print(f"çocukların kişi başına düşen payı : {kişib}")        
        
            case 5:
                num1 = int(input("1.çocuk sağ mı ölümü : "))
                num2 = int(input("1.çocuk sağ mı ölümü : "))
                num3 = int(input("1.çocuk sağ mı ölümü : "))
                num4 = int(input("1.çocuk sağ mı ölümü : "))
                num5 = int(input("1.çocuk sağ mı ölümü : "))
                
                toplam = num1 + num2 + num3 + num4 +num5
                
                kişib = gariplere / toplam
                print(f"çocukların kişi başına düşen payı : {kişib}")        
        print(f"çocukların payı ")
    elif bebek == 0:
        num2 = int(input("çocuk var mı"))
    else :
        print("geçerli bir değer giriniz")
    
        """not :
        eş 
        alt soyu 
        e
        """

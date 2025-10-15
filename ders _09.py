#mükemel sayıyı bulan program

num=int(input("sayı:"))

i=1
toplam=0
while i<num:
    if num%i==0:
        toplam=toplam+i
    i=i+1
    print(str(num),"sayısının tam bölenleri",toplam)
    if num == toplam:
            print("bu sayı mükemel sayıdır")
    else:
            print("bu sayı mükmel sayı değildir")

num1=int(input("num1:"))

num2= num1**2 #**2 x üstü 2 demek
num3= num1**3
toplam=0
while num2 <= num3:
    toplam=toplam+num2
    num2=num2+1
print(toplam)

def tamb(num2):
 bölenler=[] # sayının tam bölenlerinin ekleneceği liste
 for i in range(2,num2):
     if num2%i==0:
         bölenler.append(i)
         return bölenler
    
num1=int(input("sayi:"))
result=tamb(num1)
print("tam bölenler, :",result)
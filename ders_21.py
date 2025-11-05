#asla sayı bulma 
def asal(num2):
    flag=True
    for i in range(2,num2):
        if num2%i==0:
            flag=False
        
    return flag

num1=int(input("sayı:"))
result=asal(num1)
print(result)
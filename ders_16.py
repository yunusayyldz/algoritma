import math #kütüphane eklemek için

def dalan(arg,x):

    return math.pi*arg*arg*x

r=float(input("değer:"))
x=float(input("derinlik:"))
sonuç=dalan(r,x)

print(sonuç)

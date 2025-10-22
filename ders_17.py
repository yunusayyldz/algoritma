import math #kütüphane eklemek için

def dalan(arg,de):

    bolme=arg//de
    mod=arg%de
    sonuc1="f{arg}/{de} bol={bolme} kalan={mod}"
    return

r=float(input("değer:"))
x=float(input("derinlik:"))

sonuç=dalan(r,x)

print(sonuç)
#tekrar bak 

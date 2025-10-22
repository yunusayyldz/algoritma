import math #kütüphane eklemek için

def der(arg):

    sonuç1=math.sqrt(arg)
    return round(sonuç1,2)
r=int(input("500 den büyük bir sayı girin"))

der(r)
sonuç=der(r)
print(sonuç)

#buda başka çözüm yolu

def kokal(arg):
    
    return round(math.sqrt(arg,2))

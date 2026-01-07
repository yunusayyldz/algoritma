metin = input("buyrun: ")

yeni = []
for kelime in metin.split():
    ilk = kelime[0]
    yıldız = "*" * (len(kelime)-1)
    maske = ilk + yıldız
     
    yeni.append(maske)
    
sonuç = "".join(yeni)
print(sonuç)

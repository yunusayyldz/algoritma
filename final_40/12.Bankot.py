banknot = [200, 100, 50, 20, 10, 5, 1]

para = int(input("Lütfen para miktarını giriniz: "))

for değer in banknot:

    adet = para // değer

    if adet > 0:
        print(adet,"x",değer)
        
        para = para % değer

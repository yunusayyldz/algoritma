import random
rasgele = random.randint(1, 100)
sayaç = 0 
while True :
    tahmin = int(input("tahmin:"))
    sayaç += 1
    if tahmin > rasgele:
        print("biraz daha aşağa in")
    elif tahmin < rasgele :
        print("biraz daha yukarı çık")
    else:
        print("tebrikler")
        print(sayaç,". denemede buldunuz")
        break
    

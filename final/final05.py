sayi = int(input("sayı giriniz:"))
birler=["","bir","iki","üç","dört","beş"]
onlar=["","on","yirmi","otuz"]
yüzler = ["","yüz","ikiyüz","üçyüz"]

yüzlük = sayi // 100
onluk = (sayi % 100) // 10
birlik = sayi % 10

print(yüzler[yüzlük],onlar[onluk],birler[birlik])

birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar  = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

girilen_sayi = int(input("Lütfen iki basamaklı bir sayı giriniz: "))

onlar_basamagi = girilen_sayi // 10  
birler_basamagi = girilen_sayi % 10  

print(onlar[onlar_basamagi] + " " + birler[birler_basamagi])

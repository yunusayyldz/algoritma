# 1. Adım: Kelime haznemizi oluşturuyoruz
# 'birler' listesinin ilk elemanını boş bıraktık çünkü 0. indeks kullanılmayacak 
# ya da tam onluk sayılarda (örn: 20) sona bir şey eklenmemesi gerekiyor.
birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar  = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

# 2. Adım: Kullanıcıdan sayıyı alıyoruz
girilen_sayi = int(input("Lütfen iki basamaklı bir sayı giriniz: "))

# 3. Adım: Sayının basamaklarını buluyoruz
# Örnek sayı: 45 olsun

onlar_basamagi = girilen_sayi // 10  # 45'in içinde kaç tane 10 var? -> 4
birler_basamagi = girilen_sayi % 10  # 45'in 10'a bölümünden kalan kaç? -> 5

# 4. Adım: Kelimeleri eşleştirip yazdırıyoruz
print(onlar[onlar_basamagi] + " " + birler[birler_basamagi])

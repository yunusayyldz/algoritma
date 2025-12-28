def roma(num):
    # Değişkenlere başlangıç değeri (0) veriyoruz ki hata çıkmasın
    ikiy = yüz = elli = yirmi = on = beş = bir = 0
    
    # Döngü yerine 'if' veya doğrudan matematiksel işlem daha mantıklıdır
    if num >= 200:
        ikiy = num // 200
        num = num % 200
    if num >= 100:
        yüz = num // 100
        num = num % 100
    if num >= 50:
        elli = num // 50
        num = num % 50
    if num >= 20:
        yirmi = num // 20
        num = num % 20
    if num >= 10:
        on = num // 10
        num = num % 10
    if num >= 5:
        beş = num // 5
        num = num % 5
    if num >= 1:
        bir = num // 1
        
    return ikiy, yüz, elli, yirmi, on, beş, bir

sayi = int(input("Değiştirilmesini istediğiniz sayıyı giriniz: "))
sonuc = roma(sayi)
print("Sırasıyla adetler \n (200, 100, 50, 20, 10, 5, 1):\n ", sonuc)

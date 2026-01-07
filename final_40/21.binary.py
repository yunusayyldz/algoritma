def binarye_cevir(sayi):
    
    if sayi == 0:
        return "0"
    
    binary_karsilik = ""
    
    while sayi > 0:
        kalan = sayi % 2     
        
        binary_karsilik = str(kalan) + binary_karsilik
        
        sayi = sayi // 2   
        
    return binary_karsilik

girilen_sayi = int(input("Bir sayı giriniz: "))

sonuc = binarye_cevir(girilen_sayi)

print(f"{girilen_sayi} sayısının Binary (2'lik) karşılığı: {sonuc}")

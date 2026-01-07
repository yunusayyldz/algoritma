def ebob_ekok_hesapla(sayi1, sayi2):

    if sayi1 < sayi2:
        kucuk_sayi = sayi1
    else:
        kucuk_sayi = sayi2
    
    ebob = 1 

    for i in range(kucuk_sayi, 0, -1):

        if (sayi1 % i == 0) and (sayi2 % i == 0):
            ebob = i
            break 
            
    ekok = (sayi1 * sayi2) // ebob
    
    return ebob, ekok


s1 = int(input("Birinci sayıyı giriniz: "))
s2 = int(input("İkinci sayıyı giriniz: "))

sonuc_ebob, sonuc_ekok = ebob_ekok_hesapla(s1, s2)

print(f"--- Sonuçlar ---")
print("EBOB ",sonuc_ebob)
print("EKOK ",sonuc_ekok)

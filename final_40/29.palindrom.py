def palindrom_kontrol(metin):

    temiz_metin = ""
    
    for karakter in metin:

        if karakter.isalnum():
            temiz_metin += karakter.lower()
            
    ters_metin = temiz_metin[::-1]

    if temiz_metin == ters_metin:
        return True
    else:
        return False

girilen_cumle = input("Bir cümle veya kelime giriniz: ")

if palindrom_kontrol(girilen_cumle):
    print("✅ Bu bir Palindromdur!")
    print(f"(Temizlenmiş hali: {girilen_cumle} -> Tersten aynı)")
else:
    print("❌ Bu bir Palindrom değildir.")

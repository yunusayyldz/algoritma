metin = input("Lütfen bir cümle giriniz: ")

sayac = 0

for kelime in metin.split():
    
    if "a" in kelime or "A" in kelime :
        sayac += 1  

print(f"İçinde 'a' harfi geçen kelime sayısı: {sayac}")

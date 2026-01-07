metin = input("Lütfen bir metin giriniz: ")

print("--- İndis Numaraları ve Harfler ---")


for sira, karakter in enumerate(metin):
    
    print(f"{sira} -> {karakter}")

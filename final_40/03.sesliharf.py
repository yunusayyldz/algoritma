sesli_harfler = "aeıioöuüAEIİOÖUÜ"

sayac = 0

cumle = input("Lütfen bir cümle giriniz: ")

for harf in cumle:

    if harf in sesli_harfler:
        sayac += 1  

print("Bu cümledeki sesli harf sayısı:", sayac)

# 1. Adım: Hangi harfleri aradığımızı tanımlıyoruz
# Hem küçük hem büyük harfleri yazdık ki hatasız bulsun.
sesli_harfler = "aeıioöuüAEIİOÖUÜ"

# 2. Adım: Sayacı hazırlıyoruz (Başlangıçta 0)
sayac = 0

# 3. Adım: Kullanıcıdan cümleyi alıyoruz
cumle = input("Lütfen bir cümle giriniz: ")

# 4. Adım: Cümlenin içindeki her harfi tek tek geziyoruz
for harf in cumle:
    # Eğer o anki harf, sesli_harfler listemizin içindeyse;
    if harf in sesli_harfler:
        sayac += 1  # Sayacı 1 artır

# 5. Adım: Sonucu yazdırıyoruz
print("Bu cümledeki sesli harf sayısı:", sayac)

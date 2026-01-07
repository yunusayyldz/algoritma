# =============================================================================
# 01. Sayı > Kelime (yunusayyldz/algoritma/algoritma-main/final_40/01.sayı>kelime.py)
# =============================================================================
birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar  = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
sayi = int(input("İki basamaklı sayı: "))
print(onlar[sayi // 10] + " " + birler[sayi % 10])

# =============================================================================
# 02. Harf Rakam Simge (yunusayyldz/algoritma/algoritma-main/final_40/02.harf_rakam_sim.py)
# =============================================================================
veri = input("Karakter: ")
if veri.isalpha(): print("HARF")
elif veri.isdigit(): print("RAKAM")
else: print("SİMGE")

# =============================================================================
# 03. Sesli Harf Sayacı (yunusayyldz/algoritma/algoritma-main/final_40/03.sesliharf.py)
# =============================================================================
sesli = "aeıioöuüAEIİOÖUÜ"
cumle = input("Cümle: ")
print("Sesli harf sayısı:", sum(1 for harf in cumle if harf in sesli))

# =============================================================================
# 04. Metni Terse Çevirme (yunusayyldz/algoritma/algoritma-main/final_40/04.Mtersi.py)
# =============================================================================
print("Tersi:", input("Metin: ")[::-1])

# =============================================================================
# 05. Büyük/Küçük Harf Dönüşümü (yunusayyldz/algoritma/algoritma-main/final_40/05.Bkçevirme.py)
# =============================================================================
print(input("Metin: ").swapcase())

# =============================================================================
# 06. Türkçe -> Latin Karakter (yunusayyldz/algoritma/algoritma-main/final_40/06.latin.py)
# =============================================================================
tr_eng = {"ç":"c", "Ç":"C", "ğ":"g", "Ğ":"G", "ı":"i", "İ":"I", "ö":"o", "Ö":"O", "ş":"s", "Ş":"S", "ü":"u", "Ü":"U"}
metin = input("Metin: ")
for tr, eng in tr_eng.items(): metin = metin.replace(tr, eng)
print(metin)

# =============================================================================
# 07. İndis Numaralandırma (yunusayyldz/algoritma/algoritma-main/final_40/07.indis_num.py)
# =============================================================================
for i, k in enumerate(input("Metin: ")): print(f"{i} -> {k}")

# =============================================================================
# 08. Yer Değiştirme Şifrelemesi (yunusayyldz/algoritma/algoritma-main/final_40/08.yer_değiştirme_şifre.py)
# =============================================================================
metin = input("Metin: ")
sifreli = ""
for i in range(0, len(metin)-1, 2): sifreli += metin[i+1] + metin[i]
if len(metin) % 2 != 0: sifreli += metin[-1]
print(sifreli)

# =============================================================================
# 09. Sansürleme (yunusayyldz/algoritma/algoritma-main/final_40/09.sansür.py)
# =============================================================================
print(" ".join([k[0] + "*"*(len(k)-1) for k in input("Metin: ").split()]))

# =============================================================================
# 10. 'a' Harfi Sayısı (yunusayyldz/algoritma/algoritma-main/final_40/10.a_bulma.py)
# =============================================================================
print(sum(1 for k in input("Cümle: ").split() if "a" in k or "A" in k))

# =============================================================================
# 11. Sayı Tahmin (yunusayyldz/algoritma/algoritma-main/final_40/11.tahmin+1.py)
# =============================================================================
import random
puan = 0
while puan < 5:
    if int(input(f"Puan {puan}. Tahmin (1-5): ")) == random.randint(1, 5):
        puan += 1
        print("Doğru!")
print("Bitti.")

# =============================================================================
# 12. Banknot Hesaplama (yunusayyldz/algoritma/algoritma-main/final_40/12.Bankot.py)
# =============================================================================
banknotlar = [200, 100, 50, 20, 10, 5, 1]
para = int(input("Para: "))
for b in banknotlar:
    if para // b > 0:
        print(f"{para // b} x {b}")
        para %= b

# =============================================================================
# 13. Dik Üçgen Alanı (yunusayyldz/algoritma/algoritma-main/final_40/13.dik_üçgen.py)
# =============================================================================
print("Alan:", (float(input("Taban: ")) * float(input("Yükseklik: "))) / 2)

# =============================================================================
# 14. Sinüs Alan Formülü (yunusayyldz/algoritma/algoritma-main/final_40/14.üçgen.py)
# =============================================================================
import math
a, b, aci = float(input("a: ")), float(input("b: ")), float(input("Açı: "))
print(f"Alan: {a * b * math.sin(math.radians(aci)) / 2:.2f}")

# =============================================================================
# 15. Güçlü Şifre Kontrolü (yunusayyldz/algoritma/algoritma-main/final_40/15.güçlü_şifre.py)
# =============================================================================
p = input("Şifre: ")
ozellikler = [any(c.isupper() for c in p), any(c.islower() for c in p), 
              any(c.isdigit() for c in p), any(c in "!@#$%^&*()_+-=[]{}|;':,.<>/?\\" for c in p)]
print(f"Puan: {sum(ozellikler)}")

# =============================================================================
# 16. Manuel Yuvarlama (yunusayyldz/algoritma/algoritma-main/final_40/16.çakma_round.py)
# =============================================================================
s = float(input("Sayı: "))
print(int(s + 0.5) if s >= 0 else int(s - 0.5))

# =============================================================================
# 17. 1'den N'e Toplam (yunusayyldz/algoritma/algoritma-main/final_40/17.kulanıcıya_kadar_toplam.py)
# =============================================================================
print(sum(range(1, int(input("Kaça kadar: ")) + 1)))

# =============================================================================
# 18. EBOB ve EKOK (yunusayyldz/algoritma/algoritma-main/final_40/18.ebob_ekok.py)
# =============================================================================
s1, s2 = int(input("S1: ")), int(input("S2: "))
a, b = s1, s2
while b: a, b = b, a % b
print(f"EBOB: {a}, EKOK: {(s1*s2)//a}")

# =============================================================================
# 19. Faktöriyel (Recursive) (yunusayyldz/algoritma/algoritma-main/final_40/19.faköriyel.p)
# =============================================================================
def fak(n): return 1 if n < 2 else n * fak(n-1)
print(fak(int(input("Sayı: "))))

# =============================================================================
# 20. Kendisi Hariç En Büyük Bölen (yunusayyldz/algoritma/algoritma-main/final_40/20.k_ebob.py)
# =============================================================================
s = int(input("Sayı: "))
for i in range(s//2, 0, -1):
    if s % i == 0: print(i); break

# =============================================================================
# 21. Decimal -> Binary (yunusayyldz/algoritma/algoritma-main/final_40/21.binary.py)
# =============================================================================
s, b = int(input("Sayı: ")), ""
while s > 0: b = str(s % 2) + b; s //= 2
print(b or "0")

# =============================================================================
# 22. Onlar Basamağı Toplama (yunusayyldz/algoritma/algoritma-main/final_40/22.onlar_topla.py)
# =============================================================================
print(sum(((int(input(f"{i}. sayı: ")) // 10) % 10) * 10 for i in range(1, 11)))

# =============================================================================
# 23. En Büyük Sayı (yunusayyldz/algoritma/algoritma-main/final_40/23.En_B_10sayi.py)
# =============================================================================
print("En büyük:", max(int(input(f"{i}. sayı: ")) for i in range(1, 11)))

# =============================================================================
# 24. 1/x Bölme (yunusayyldz/algoritma/algoritma-main/final_40/24.VirgüldenS_3Basamak.py)
# =============================================================================
s = float(input("Sayı: "))
print(f"{1/s:.3f}" if s != 0 else "0 bölünmez")

# =============================================================================
# 25. Ay Mevsim (yunusayyldz/algoritma/algoritma-main/final_40/25.Aylar.py)
# =============================================================================
aylar = ["","Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
no = int(input("Ay No: "))
print(f"{aylar[no]} - {['Kış','İlkbahar','Yaz','Sonbahar'][(no%12)//3]}")

# =============================================================================
# 26. Maclaurin Sin(x) (yunusayyldz/algoritma/algoritma-main/final_40/*26.sin(x).py)
# =============================================================================
import math
x = math.radians(float(input("Derece: ")))
print(sum(((-1)**((n-1)//2)) * (x**n) / math.factorial(n) for n in range(1, 10, 2)))

# =============================================================================
# 27. Mastermind (yunusayyldz/algoritma/algoritma-main/final_40/27.sayı_bulma4B.py)
# =============================================================================
import random
s = "".join(map(str, random.sample(range(10), 4)))
while s[0] == '0': s = "".join(map(str, random.sample(range(10), 4)))
while True:
    t = input("4 haneli: ")
    arti = sum(1 for i in range(4) if t[i] == s[i])
    eksi = sum(1 for k in t if k in s) - arti
    print(f"+{arti}, -{eksi}")
    if arti == 4: break

# =============================================================================
# 28. Asal Kontrol (yunusayyldz/algoritma/algoritma-main/final_40/*28.asal.py)
# =============================================================================
s = int(input("Sayı: "))
print("Asal" if s > 1 and all(s % i != 0 for i in range(2, int(s**0.5)+1)) else "Değil")

# =============================================================================
# 29. Palindrom (yunusayyldz/algoritma/algoritma-main/final_40/29.palindrom.py)
# =============================================================================
t = "".join(c.lower() for c in input("Metin: ") if c.isalnum())
print("Palindrom" if t == t[::-1] else "Değil")

# =============================================================================
# 30. Asal Liste (yunusayyldz/algoritma/algoritma-main/final_40/30.asal_liste.py)
# =============================================================================
limit = int(input("Sınır: "))
print([s for s in range(2, limit + 1) if all(s % i != 0 for i in range(2, int(s**0.5)+1))])

# =============================================================================
# 31. Liste İstatistik (yunusayyldz/algoritma/algoritma-main/final_40/31. ortlama_min_maks.py)
# =============================================================================
L = list(map(int, input("Sayılar: ").split()))
print(f"Ort: {sum(L)/len(L):.2f}, Min: {min(L)}, Max: {max(L)}")

# =============================================================================
# 32. Kelime Frekansı (yunusayyldz/algoritma/algoritma-main/final_40/32.kelime_freknas.py)
# =============================================================================
m = input("Metin: ").lower()
for k in ".,!?;:()-": m = m.replace(k, "")
D = {}
for w in m.split(): D[w] = D.get(w, 0) + 1
print(D)

# =============================================================================
# 33. Ters Liste (yunusayyldz/algoritma/algoritma-main/final_40/33.ters_liste.py)
# =============================================================================
L = input("Liste: ").split()
print([L[i] for i in range(len(L)-1, -1, -1)])

# =============================================================================
# 34. Mükemmel Sayı (yunusayyldz/algoritma/algoritma-main/final_40/*34.mükemel_sayı.py)
# =============================================================================
s = int(input("Sayı: "))
print("Mükemmel" if s > 1 and sum(i for i in range(1, s//2 + 1) if s % i == 0) == s else "Değil")

# =============================================================================
# 35. Kesişim Birleşim (yunusayyldz/algoritma/algoritma-main/final_40/35.kes_birleşim.py)
# =============================================================================
s1, s2 = set([1,2,3,4,5]), set([4,5,6,7,8])
print(f"Kesişim: {s1 & s2}, Birleşim: {s1 | s2}")

# =============================================================================
# 36. Tekrar Edenler (yunusayyldz/algoritma/algoritma-main/final_40/36.tekrar_eleman.py)
# =============================================================================
L = input("Veri: ").split()
print(set([x for x in L if L.count(x) > 1]))

# =============================================================================
# 37. Sezar Şifre (yunusayyldz/algoritma/algoritma-main/final_40/37.Şifre_çöz.py)
# =============================================================================
def sezar(t, k):
    res = ""
    for c in t:
        if c.isalpha():
            base = 65 if c.isupper() else 97
            res += chr((ord(c) - base + k) % 26 + base)
        else: res += c
    return res
op = input("1-Şifrele 2-Çöz: ")
print(sezar(input("Metin: "), int(input("Anahtar: ")) * (1 if op=='1' else -1)))

# =============================================================================
# 38. Not Ortalaması (yunusayyldz/algoritma/algoritma-main/final_40/38.öğrenci_ortl.py)
# =============================================================================
n = [float(input(f"{i+1}. Not: ")) for i in range(int(input("Kaç öğrenci: ")))]
print(f"Ort: {sum(n)/len(n):.2f}, Max: {max(n)}, Min: {min(n)}")

# =============================================================================
# 39. Armstrong Sayısı (yunusayyldz/algoritma/algoritma-main/final_40/39.Armstrong.py)
# =============================================================================
s = input("Sayı: ")
print("Armstrong" if sum(int(d)**len(s) for d in s) == int(s) else "Değil")

# =============================================================================
# 40. Metin Analizi (yunusayyldz/algoritma/algoritma-main/final_40/40.kulanıcı_hepsi_bir.py)
# =============================================================================
m = input("Metin: ")
h = sum(c.isalpha() for c in m)
r = sum(c.isdigit() for c in m)
b = sum(c.isspace() for c in m)
print(f"Harf: {h}, Rakam: {r}, Boşluk: {b}, Özel: {len(m)-h-r-b}")

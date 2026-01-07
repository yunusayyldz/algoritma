import math e

a = float(input("Birinci kenar uzunluğunu (a) giriniz: "))
b = float(input("İkinci kenar uzunluğunu (b) giriniz: "))
aci = float(input("Aradaki açıyı (derece olarak) giriniz: "))

alan = a * b * math.sin(aci * math.pi / 180) / 2

print(f"Üçgenin Alanı: {alan:.2f}")

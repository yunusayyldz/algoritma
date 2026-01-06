def kume_islemleri(liste_a, liste_b):
    # 1. Adım: Listeleri kümeye (set) çeviriyoruz
    # Böylece hem kopyalar silinir hem de matematiksel işlem yapılabilir.
    kume_a = set(liste_a)
    kume_b = set(liste_b)
    
    # 2. Adım: Kesişim (Intersection) -> İkisinde de olanlar
    # "&" operatörü veya .intersection() metodu kullanılır.
    kesisim = kume_a & kume_b
    
    # 3. Adım: Birleşim (Union) -> Hepsi (Tekrarsız)
    # "|" operatörü veya .union() metodu kullanılır.
    birlesim = kume_a | kume_b
    
    # Sonuçları tekrar listeye çevirip döndürüyoruz
    return list(kesisim), list(birlesim)

# --- Test Edelim ---
# Örnek Listeler
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

sonuc_kesisim, sonuc_birlesim = kume_islemleri(l1, l2)

print(f"Liste 1: {l1}")
print(f"Liste 2: {l2}")
print("-" * 30)
print(f"Kesişim (Ortaklar): {sonuc_kesisim}")  # Beklenen: [4, 5]
print(f"Birleşim (Hepsi)  : {sonuc_birlesim}") # Beklenen: 1'den 8'e kadar hepsi

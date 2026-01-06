# 1. Adım: Fonksiyonumuzu tanımlıyoruz
def sayilari_topla(bitis_sayisi):
    # Toplamı tutacak 'sepetimizi' hazırlıyoruz. Başlangıçta boş (0).
    toplam = 0
    
    # 2. Adım: 1'den başlayıp bitiş sayısına kadar dönüyoruz
    # DİKKAT: range fonksiyonunda son sayı dahil edilmez.
    # Bu yüzden (bitis_sayisi + 1) yazıyoruz ki o sayıyı da kapsasın.
    for sayi in range(1, bitis_sayisi + 1):
        toplam += sayi  # Sepete o anki sayıyı ekle (toplam = toplam + sayi)
        
    # 3. Adım: Sepette biriken sonucu geri gönderiyoruz
    return toplam

# --- Ana Program ---

kullanici_sayisi = int(input("Kaça kadar toplamak istersiniz? : "))

# Fonksiyonu çağırıp sonucu alıyoruz
sonuc = sayilari_topla(kullanici_sayisi)

print(f"1'den {kullanici_sayisi} sayısına kadar olanların toplamı: {sonuc}")

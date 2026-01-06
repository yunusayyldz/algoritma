def not_analizi():
    print("--- Öğrenci Not Analiz Programı ---")
    
    # 1. Adım: Kaç öğrenci olduğunu öğren
    # (Döngünün kaç kere döneceğini belirlemek için)
    try:
        ogrenci_sayisi = int(input("Sınıfta kaç öğrenci var?: "))
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")
        return

    # Eğer 0 veya negatif girilirse programı durdur
    if ogrenci_sayisi <= 0:
        print("Hesaplama yapmak için en az 1 öğrenci olmalıdır.")
        return

    # Notları biriktireceğimiz boş liste
    notlar = []

    # 2. Adım: Notları tek tek al
    for i in range(ogrenci_sayisi):
        while True:
            try:
                # Kullanıcıya "1. Öğrenci", "2. Öğrenci" gibi sormak için i+1 kullanıyoruz
                not_girisi = float(input(f"{i+1}. Öğrencinin notunu giriniz: "))
                
                # Notun 0-100 arasında olup olmadığını kontrol edelim
                if 0 <= not_girisi <= 100:
                    notlar.append(not_girisi)
                    break # Geçerli not girildiyse while döngüsünden çık, sıradaki öğrenciye geç
                else:
                    print("Lütfen 0 ile 100 arasında bir not giriniz!")
            except ValueError:
                print("Hata: Lütfen sayısal bir değer giriniz.")

    # 3. Adım: Hesaplamalar
    # Python'da bu işlemler için uzun uzun döngü kurmaya gerek yoktur.
    
    en_yuksek = max(notlar)       # Listenin kralını bulur
    en_dusuk = min(notlar)        # Listenin en küçüğünü bulur
    ortalama = sum(notlar) / len(notlar)  # Toplam / Adet

    # 4. Adım: Sonuçları Yazdır
    print("-" * 30)
    print("📊 SINIF İSTATİSTİKLERİ")
    print("-" * 30)
    print(f"Öğrenci Sayısı : {ogrenci_sayisi}")
    print(f"En Yüksek Not  : {en_yuksek}")
    print(f"En Düşük Not   : {en_dusuk}")
    print(f"Sınıf Ortalaması: {ortalama:.2f}") # Virgülden sonra 2 basamak göster

# Programı başlat
not_analizi()

#örnek = "kabak" düz halide ters halide aynı olana deniyor palindrom
def palindrom_kontrol(metin):
    # 1. Adım: Temiz bir versiyon oluştur (Sadece harfler ve sayılar)
    temiz_metin = ""
    
    for karakter in metin:
        # isalnum() -> "Is Alpha Numeric?" (Harf veya Sayı mı?)
        # Eğer karakter harf veya sayıysa, küçültüp listeye ekle.
        # Böylece boşluklar ve noktalama işaretleri elenir.
        if karakter.isalnum():
            temiz_metin += karakter.lower()
            
    # 2. Adım: Metnin tersini al
    # Python'da [::-1] bir metni baştan sona ters çevirir.
    ters_metin = temiz_metin[::-1]
    
    # 3. Adım: Kıyasla ve sonucu döndür
    if temiz_metin == ters_metin:
        return True
    else:
        return False

# --- Ana Program ---
girilen_cumle = input("Bir cümle veya kelime giriniz: ")

if palindrom_kontrol(girilen_cumle):
    print("✅ Bu bir Palindromdur!")
    print(f"(Temizlenmiş hali: {girilen_cumle} -> Tersten aynı)")
else:
    print("❌ Bu bir Palindrom değildir.")

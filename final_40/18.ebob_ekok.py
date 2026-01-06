def ebob_ekok_hesapla(sayi1, sayi2):
    # 1. ADIM: EBOB BULMA
    # Önce küçük sayıyı bulalım ki döngü kısa sürsün
    if sayi1 < sayi2:
        kucuk_sayi = sayi1
    else:
        kucuk_sayi = sayi2
    
    ebob = 1 # Varsayılan değer
    
    # Küçük sayıdan başlayıp 1'e doğru geriye sayıyoruz
    for i in range(kucuk_sayi, 0, -1):
        # Eğer 'i' hem sayı1'i hem sayı2'yi tam bölüyorsa EBOB odur.
        if (sayi1 % i == 0) and (sayi2 % i == 0):
            ebob = i
            break # En büyüğü bulduk, artık döngüyü kırıp çıkabiliriz.
            
    # 2. ADIM: EKOK BULMA (Matematiksel Formül)
    # // kullanarak tam sayı sonucu istiyoruz (virgül olmasın diye)
    ekok = (sayi1 * sayi2) // ebob
    
    # İki değeri birden paketleyip gönderiyoruz
    return ebob, ekok

# --- Ana Program ---

s1 = int(input("Birinci sayıyı giriniz: "))
s2 = int(input("İkinci sayıyı giriniz: "))

# Fonksiyondan dönen iki değeri, virgülle ayırarak iki değişkene alıyoruz
sonuc_ebob, sonuc_ekok = ebob_ekok_hesapla(s1, s2)

print(f"--- Sonuçlar ---")
print(f"EBOB ({s1}, {s2}) = {sonuc_ebob}")
print(f"EKOK ({s1}, {s2}) = {sonuc_ekok}")

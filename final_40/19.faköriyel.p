def faktoriyel_recursive(n):
    # 1. ADIM: DURMA NOKTASI (Base Case)
    # Bu kısım olmazsa fonksiyon sonsuza kadar çalışır ve hata verir.
    # 0! ve 1! matematiksel olarak 1'dir.
    if n == 0 or n == 1:
        return 1
    
    # 2. ADIM: KENDİNİ ÇAĞIRMA (Recursive Step)
    # Sayıyı alıyoruz ve fonksiyonun kendisini (bir eksiğiyle) tekrar çağırıyoruz.
    else:
        return n * faktoriyel_recursive(n - 1)

# --- Test Edelim ---
sayi = int(input("Faktöriyeli alınacak sayıyı giriniz: "))

# Negatif sayılarda faktöriyel olmaz, basit bir önlem alalım.
if sayi < 0:
    print("Negatif sayıların faktöriyeli hesaplanamaz.")
else:
    sonuc = faktoriyel_recursive(sayi)
    print(f"{sayi}! = {sonuc}")

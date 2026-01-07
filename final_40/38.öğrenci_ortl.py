def sınıf():    
    try:
        adet = int(input("Öğrenci sayısı: "))
        
        notlar = [float(input(f"{i+1}. Notu giriniz: ")) for i in range(adet)]
    
        if notlar:
            print(f"-"*30)
            print(f"Ortalama : {sum(notlar)/len(notlar):.2f}")
            print(f"En Yüksek: {max(notlar)} \nEn Düşük : {min(notlar)}")
        else:
            print("Not girilmedi.")
    
    except ValueError:
        print("Hatalı giriş yaptınız, lütfen sayı girin!")
sınıf()

print("Miras Hesaplama Programı (1=Evet, 0=Hayır)")

es = int(input("Eş sağ mı? (1/0): "))
cocuk_var = int(input("Çocuk var mı? (1/0): "))


# -----------------------
# 1) EŞ SAĞSA
# -----------------------
if es == 1:

    # --- KOŞUL 1: EŞ + ÇOCUK VAR ---
    if cocuk_var == 1:
        print("Eş sağ + çocuk var")
        es_pay = 1/4
        cocuk_pay_kalan = 3/4

        adet = int(input("Çocuk sayısı: "))
        kollar = []

        for i in range(adet):
            durum = int(input(f"{i+1}. çocuk sağ mı? (1=sağ, 0=ölü): "))
            if durum == 1:
                kollar.append(1)
            else:
                torun = int(input(f"{i+1}. çocuk ölmüş → kaç çocuğu var?: "))
                kollar.append(torun)

        toplam_kol = sum(kollar)

        print(f"Eş payı = {es_pay}")
        print("Çocuklara kalan 3/4 aşağıdaki şekilde bölünür:")

        for i, kol in enumerate(kollar):
            pay = (cocuk_pay_kalan * kol) / toplam_kol
            print(f"{i+1}. kol payı = {pay}")

    # --- KOŞUL 2 ve 3: EŞ SAĞ + ÇOCUK YOK ---
    else:
        print("Eş sağ + çocuk yok")

        z1 = int(input("1. zümrede (anne, baba, kardeş) sağ var mı? (1/0): "))
        if z1 == 1:
            print("→ Koşul 2: Eş 1/2 + 2. zümre 1/2")
            print("Eş = 1/2")
            print("2. zümre = 1/2")

        else:
            z2 = int(input("2. zümre yok → 3. zümre var mı? (1/0): "))
            if z2 == 1:
                print("→ Koşul 3: Eş 3/4 + 3. zümre 1/4")
                print("Eş = 3/4")
                print("3. zümre = 1/4")
            else:
                print("Hiç kimse yok → Devlete kalır.")


# -----------------------
# 2) EŞ YOKSA
# -----------------------
else:

    # KOŞUL 4 ve 5 – ÇOCUK VARSA
    if cocuk_var == 1:

        adet = int(input("Çocuk sayısı: "))

        if adet == 1:
            print("→ Koşul 5: Tek çocuk tüm mirası alır (1)")
        else:
            print("→ Koşul 4: Kollar eşit bölünür")

            kollar = []
            for i in range(adet):
                durum = int(input(f"{i+1}. çocuk sağ mı? (1/0): "))
                if durum == 1:
                    kollar.append(1)
                else:
                    torun = int(input(f"{i+1}. çocuk ölü → kaç çocuğu var?: "))
                    kollar.append(torun)

            toplam_kol = sum(kollar)

            for i, kol in enumerate(kollar):
                pay = kol / toplam_kol
                print(f"{i+1}. kola düşen pay = {pay}")

    # -------------------------------
    # EŞ YOK + ÇOCUK DA YOK
    # -------------------------------
    else:
        print("Eş yok + çocuk yok")

        z1 = int(input("1. zümre (anne, baba, kardeş) sağ mı? (1/0): "))

        if z1 == 1:
            anne = int(input("Anne sağ mı? (1/0): "))
            baba = int(input("Baba sağ mı? (1/0): "))

            # KOŞUL 7
            if anne == 1 and baba == 1:
                print("→ Koşul 7: Anne 1/2, Baba 1/2")

            # KOŞUL 9
            elif baba == 1 and anne == 0:
                print("→ Koşul 9: Baba 1/2, kardeşler 1/2")

                kardes_say = int(input("Kardeş sayısı: "))
                kollar = []

                for i in range(kardes_say):
                    sag = int(input(f"{i+1}. kardeş sağ mı? (1/0): "))
                    if sag == 1:
                        kollar.append(1)
                    else:
                        alt = int(input(f"{i+1}. kardeş ölü → kaç çocuğu var?: "))
                        kollars.append(alt)

                toplam = sum(kollar)
                for i, kol in enumerate(kollar):
                    pay = (1/2) * kol / toplam
                    print(f"{i+1}. kola düşen pay = {pay}")

            # KOŞUL 8
            else:
                print("→ Koşul 8: Anne baba ölü → kardeşler pay alır")

        else:
            z2 = int(input("2. zümre yok → 3. zümre var mı? (1/0): "))

            # KOŞUL 10
            if z2 == 1:
                print("→ Koşul 10: 3. zümre 1/4 alır")

            else:
                print("→ Koşul 11: Miras devlete kalır.")
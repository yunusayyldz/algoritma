toplam = 0

while True:
    num=int(input("sayı:"))
    
    toplam = toplam + num
    #while döngüsü burada sonsuza kadar durmadan devam eder ama biz if(break dahil buna) ile o döngüyü kırıyoruz
    print("toplam:",toplam)
    if toplam > 50 :
        break 
    
    toplam =0
    while toplam<50:
            num=int(input("sayı:"))
            toplam=toplam+num
            print("toplam",toplam)
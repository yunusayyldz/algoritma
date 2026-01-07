def ebob_ekok(s1, s2):
    a, b = s1, s2

    while b:
        a, b = b, a % b  
    
    ebob = a
    ekok = (s1 * s2) // ebob
    return ebob, ekok
        
s1 = int(input("1. Sayı: "))
s2 = int(input("2. Sayı: "))

ebob, ekok = ebob_ekok(s1, s2)
print(f"EBOB: {ebob}\nEKOK: {ekok}")

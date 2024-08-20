n = int(input("Moi nhap so nam: "))
ktra = n%2
if ktra == 0:
    print(f"{n}la so chan")
else:
    print(n,"la so le")
#tinh nam nhuan
n = int(input("nhap so nam: "))
if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print(f"{n}la nam nhuan")
else:
    print(f"{n} khong la nam nhuan")

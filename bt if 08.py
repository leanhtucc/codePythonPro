n = int(input("Moi nhap so thang: "))
if n in (1,3,5,7,8,10,12):
    print(f"thang {n} co 31 ngay")
elif n in (4,6,9,11):
    print(f"thang {n} co 30 ngay")
elif n==2:
    n = int(input("Moi nhap them so nam: "))
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        print(f"{n}la nam nhuan")
    else:
        print(f"{n} khong la nam nhuan ")
else:
    print("ban da nhap sai so thang")
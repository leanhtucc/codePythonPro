from math import*
so=int(input("Nhập số: "))
def kiem_tra_so_nguyen_to(so):
    if so < 2:
        return False
    for i in range(2, isqrt(so) +1):
        if i%so==0:
            return False
        else:
            return True
def tinh_tong_chu_so(so):
    tong=0
    for chu_so in str(so):
        tong+= int(chu_so)
        return tong
tong_chu_so= tinh_tong_chu_so(so)
la_nguyen_to= kiem_tra_so_nguyen_to(tong_chu_so)
if la_nguyen_to:
    print(f"Tong cua {so} la so nguyen to")
else:
    print(f"Tong cua {so} khog la so nguyen to")

def tinh_tong(n):
    if n > 0:
        return n + tinh_tong(n-1)
    return 0
n=int(input("nhap so: "))
if n < 0:
    print("Nhap so tu nhien!")
else:
    print(tinh_tong(n))
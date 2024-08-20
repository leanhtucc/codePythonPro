from math import*
def kiem_tra_nguyen_to(so):
    if so < 2:
        return False
    for i in range(2, isqrt(so) + 1):
        if so % i == 0:
            return False
    return True

def tinh_tong_chu_so(so):
    tong = 0
    for chu_so in str(so):
        tong += int(chu_so)
    return tong

# Nhập số từ người dùng
so = int(input("Nhập số: "))

# Tính tổng các chữ số của số nhập vào
tong_chu_so = tinh_tong_chu_so(so)

# Kiểm tra tổng các chữ số có phải là số nguyên tố hay không
la_nguyen_to = kiem_tra_nguyen_to(tong_chu_so)

if la_nguyen_to:
    print(f"Tổng các chữ số của {so} là số nguyên tố.")
else:
    print(f"Tổng các chữ số của {so} không là số nguyên tố.")

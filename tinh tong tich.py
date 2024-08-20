danh_sach_1=[1,2,3,4,5,6,7,8,9]
danh_sach_2=[10,11,12,13,14,15,16]
def tinh_tong(danh_sach):
    tong=0
    for so in danh_sach:
        tong+= so
        return tong
def tinh_tich(danh_sach):
    tich=0
    for so in danh_sach:
        tich+= so
        return tich
tinh_tong_1= tinh_tong(danh_sach_1)
tinh_tich_1= tinh_tich(danh_sach_2)

tinh_tong_2= tinh_tong(danh_sach_2)
tinh_tich_2= tinh_tich(danh_sach_2)

print(f"tong cua danh sach 1: {tinh_tong_1}")
print(f"tich cua danh sach 1: {tinh_tich_1}")

print(f"tong cua danh sach 2: {tinh_tong_2}")
print(f"tich cua danh sach 2: {tinh_tich_2}")

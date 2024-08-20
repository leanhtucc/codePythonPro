str1 ="English = 78 Science = 83 Math = 68 History = 65"
tach = str1.split()
s=0
dem=0
for i in tach:
    if i.isdigit():
        s=s+int(i)
        dem+=1
print(f"tong cac so trong chuoi tren la: {s}")
print(f"trung binh cong cac so trong chuoi tren la: {s/dem}")
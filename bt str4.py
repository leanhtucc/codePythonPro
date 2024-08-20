b ="university of technology and education"
for i in range(len(b)):
    if b[i]=="a":
        print("vi tri ky tu a la:",i,end="\n ")

# nhan doi tu hello
a ="hello"
s = ""
for i in a:
    s=s+i+i
print(s)
#dem phu am
n = "ban hay nhap mot chuoi ky tu"
dem = 0
dem_2 = 0
for i in n:
    if i in ("u,e,o,a,i"):
        dem+=1
    else:
        i!=""
        dem_2+=1
print(f"tong so nguyen am la: {dem}")
print(f"tong so phu am la: {dem_2}")

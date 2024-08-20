lst = []
n = int(input('Nhập vào số phần tử: '))
dem = 0
while dem < n:
    dem = dem + 1
    a = int(input('Nhập vào phần tử: '))
    lst.append(a)
    print('list bạn vừa nhập: ',lst)
#chi ra các số bé hơn 5
dem2 = 0
for i in lst:
    if i<5:
        dem2 = dem2 + 1
print("Số chữ số bé hơn 5 là: ", dem2)
# in ra vị trí index
for j in range(len(lst)):
    print(j)
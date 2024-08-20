lst = []
n = int(input('Nhập vào sóo phần tử: '))
dem = 0
while dem < n:
    dem = dem + 1
    a = int(input('Nhập vào phần tử: '))
    lst.append(a)
    print('list bạn vừa nhập: ', lst)

    lst_2 = []
    for i in lst:
        lst_2.append(i ** 2)
        print(lst_2)
# xác định bao nhiêu phần tử lớn hơn 50
dem2 = 0
for i in lst_2:
    if i > 50:
        dem2 += 1
        print(f'list mới có {dem2} lớn hơn 50')

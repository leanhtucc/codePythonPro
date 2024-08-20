lst = [1,2,3,5,9,10,11]
lst_max = []
lst_min = []
for i in lst:
    if i == max(lst):
        continue
    else:
        lst_max.append(i)
for j in lst:
    if j == min(lst):
        continue
    else:
        lst_min.append(j)
print('Giá trị lớn thứ 2 là: ', max(lst_max))
print('Giá trị nhỏ thứ 2 là: ', min(lst_min))
max2=max(lst_max)
min2=min(lst_min)
for i in range(len(lst)):
    if lst[i]==max2:
        print(i)
for j in range(len(lst)):
    if lst[j]==min2:
        print(j)
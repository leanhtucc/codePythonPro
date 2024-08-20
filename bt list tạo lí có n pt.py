from random import randrange
n = int(input('Nhập số phần tử: '))
lst = [0]*n
for i in range(n):
    lst[i]=randrange(1,101)
    print(lst)

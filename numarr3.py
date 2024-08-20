import numpy as np
L = [[34,43,73],[82,22,12],[53,94,66]]
a=np.array(L)
min=max=a[0,0]
for i in a:
    for j in i:
        if j <min:
            min=j
        elif j> max:
            max=j
print(f"giá trị nhỏ nhất trong ma trận:{min} ")
print(f"giá trị lớn nhất trong ma trận:{max}")
for i in range(a.shape[0]):
    for j in range(a.shape[2]):
        if a[i,j]== max:
            print(f"vị trí index lớn nhất trong ma trận:{i,j}")
        elif a[i,j]== min:
            print(f"vị trí index nhỏ nhất trong ma trận:{i,j}")
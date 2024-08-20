import numpy as np
arr=np.zeros((8,8))
for colum in range(arr.shape[1]):
    if colum % 2 !=0:
        arr[0,7:colum]=1
    else:
        arr[7,colum]=1


print(arr)
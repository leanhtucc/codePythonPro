ds=[1,2,3,4,5,6,7,8,9]
new_arr = []
for i in range(len(ds)):
    if i % 2 == 0:
        new_arr.append(ds[i])
print(new_arr)


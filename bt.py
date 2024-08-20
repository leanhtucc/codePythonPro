def sum_and_product(arr):
    total = sum(arr)
    product = 1
    for num in arr:
        product *= num
    return total, product
ds=[1,2,3,6,8]
print(sum_and_product(ds))

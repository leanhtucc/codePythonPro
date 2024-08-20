mang = [1,2,3,4,5,6,7,8,9]
length=len(mang)
if length%2==0:
    for i in range(0,length,2):
        mang[i],mang[i+1]=mang[i+1],mang[i]
    else:
        cuoi=mang.pop()
print(mang)
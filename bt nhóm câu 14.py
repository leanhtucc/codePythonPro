#câu 14
mang=[1,2,3,4,5,6,7,8,9,10]
s=len(mang)
d=s-1
if s%2==0:
    for i in range (0,s,2):
        mang[i],mang[i+1]=mang[i+1],mang[i]
else:
    for i in range (0,d,2):
        mang[i], mang[i + 1] = mang[i + 1], mang[i]
print(mang)
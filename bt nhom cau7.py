from math import*
list = [1,2,3,4,5,6,7,8,9]
new=[]
def prime(i):
    if i<2:
        return False
    for j in range(2,isqrt(i)+1):
        if i%j==0:
            return False
    return True
for i in range(len(list)):
    if prime(i)==False:
        new.append(list[i])
print(f"day so bi loai bo la:{new}")
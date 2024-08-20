#câu 15
from math import *
list=[1,2,4,2,4,5,6,91,97,33]
nt=[]
kont=[]
def prime(i):
    if i<2:
        return False
    for j in range(2,isqrt(i)+1):
        if i%j==0:
            return False
    return True
    for i in list:
        if prime(i):
            nt.append(i)
        else:
            kont.append(i)
    print('các số là số nguyên tố là',*set(nt))
    print('các số ko phải là số nguyên tố là',*set(kont))
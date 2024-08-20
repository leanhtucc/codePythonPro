import math
a, b, c=map(float,input().split())
if a==0:
    if b==0:
        if c==0:
            print("Phuong trinh co vo so nghiem")
        print("Phuong trinh vo nghiem")
    print("Phuong trinh co nghiem duy nhat la \nx ={}".format(-c/b))
else:
    dental = b**2 -4 * a * c
    if dental > 0:
        x1=(-b + math.sqrt(dental)) / (2*a)
        x2=(-b - math.sqrt(dental)) / (2*a)
        print("Phuong trinh co 2 nghiem phan biet la: \nx1 ={} \nx2 = {}".format(x1,x2))
    if dental ==0:
        x= -b / (2*a)
        print("Phuong trinh co nghiem kep la \nx1 = x2= {}".format(x))
    else:
        print("Phuong trinh vo nghiem")
n=int(input("Nhập một số: "))
if n < 1 or n > 9:
    print("Vui lòng nhập số từ 1 đến 9")
else:
    for i in range(1, n+1):
        line= ""
        for j in range(1, i+1):   #for j in range(n-i, 0, -1)  print(j, end=" ")  print()
            line="{} {}".format(line, j)
print(line)
n=input("Nhập dãy số cần tách: ")
s1=""
s2=""
for i in n:
    if i.isdigit():
        s1+=i
    elif i.isalpha():
        s2+=i
print("dãy số là: ", s1)
print("dãy chữ là: ", s2)

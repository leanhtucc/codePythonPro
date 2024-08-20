n ="abc123"
n = input("Mời nhập mk ") #abc123
x = bool
y = bool
while True:
    for i in n:
        if i.isdigit():
            x = True
            break
        else:
            x = False
    for i in n:
        if i.isalpha():
            y = True
            break
        else:
            y = False
    if len(n)<6 or x==False or y==False:
        n=input("Nhập lại mk, ít nhất 6 ký tự, ít nhất 1 chữ cái và 1 số")
    else:
        print("Mật khẩu hợp lệ")
        break
# cho nguoi dung nhap mk
s = input("Mời đăng nhập hệ thống: ")
dem=0
while s!=n:
    dem=dem+1
    s=input(f"Mời nhập lại mật khẩu, nhập sai {dem}/5 lần: ")
    if dem==5:
        print("Bạn đã nhập sai quá 5 lần, khóa đăng nhập")
        break
else:
    print("đăng nhập thành công")
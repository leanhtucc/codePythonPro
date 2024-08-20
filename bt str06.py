#mã hóa bảng trữ cái
a="abcdefghiklmnopqrstuvwxyz"
b="zxcvbnmasdfghjklqwertyuiop"
n=input("Nhập vào ký tự từ a-z đẻ mã hóa:")
s=""
for i in n:
    index=a.find(i)
    s=s+b[index]
print(s)

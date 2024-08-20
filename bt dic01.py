#bai1 nhập password

dic={"user1":"123456",
"user2":"123456",
"user3":"123456",
"user4":"123456",
"user5":"123456",
"user6":"123456",
"user7":"123456",
"user8":"123456",
"user9":"123456",
"user10":"123456"}


user=input("Nhập username: ")
password=input("Nhập password: ")
if user not in dic:
    print("password không tồn tại")
else:
    if user != password:
        print("password sai")
    else:
        print("password dúng")

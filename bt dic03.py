d=[{"name":"Tuan","phone":"555-1414","email":"galailaptrinh@gmail.com"},
    {"name":"Hung","phone":"555-1618","email":"galaixapxinh@gmail.com"},
    {"name":"Trung","phone":"555-3141","email":""},
    {"name":"Hoang","phone":"555-2718","email":"loli@gmail.com"},
]
print("Các user có số điện thoại kết thúc là 8")
for dong in d:
    phone_check=dong["phone"]
    if phone_check[-1]=="8":
        name_check=dong["name"]
        phone_check=dong["phone"]
        email_check=dong["email"]
        print("-"*50)
        print("Tên: ", name_check)
        print("Số điện thoại: ", phone_check)
        print("email: ", email_check)
print("Các user o có địa chỉ email")
for dong in d:
    if dong["email"] == "":
        name_show=dong["name"]
        phone_show=dong["phone"]
        email_show=dong["email"]
        print("*"*50)
        print("Tên: ", name_show)
        print("Số điện thoại: ", phone_show)
        print("email: ", email_show)
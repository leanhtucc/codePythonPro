mybooks=[
{"Title": "Android App Development", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "25000","Published_Year": "2017"},
{"Title": "Python", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "23000", "Published_Year": "2019"},
{"Title": "JavaScript", "Author": "Pham Dieu",
"Publisher": "SSS", "Price": "38000","Published_Year": "2018"},
{"Title": "HTML5", "Author": "Man Nhi",
"Publisher": "HCM", "Price": "33000", "Published_Year": "2012"},
{"Title": "Compiler", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "24000","Published_Year": "2011"},
{"Title": "C language", "Author": "Man Nhi",
"Publisher": "SSS", "Price": "29000","Published_Year": "2010"},
{"Title": "Programming Linguistics", "Author": "Pham Dieu",
"Publisher": "HCM","Price": "41000", "Published_Year": "2009"},
{"Title": "C# language", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "42000","Published_Year": "2013"},
{"Title": "App Inventor", "Author": "Man Nhi",
"Publisher": "LD", "Price": "30000","Published_Year": "2015"},
]
check=False
while check==False:
    chon=input("""Chọn để tìm kiếm: 
        1.Title
        2.Author
        3.Publisher
        selec(1,2,3):
""")
    if chon=="1":
        kwd="Title"
        break
    elif chon=="2":
        kwd="Author"
        break
    elif chon=="3":
        kwd="Publisher"
        break
    else:
        print("inval input")
        check=False
dem=0
inputkw=input("Nhâpj keyword để tìm kiếm: ")
for dong in mybooks:
    if inputkw==dong[kwd]:
        print("Title: ", dong["Title"])
        print("Author: ", dong["Author"])
        print("Publisher: ",dong["Publisher"])
        dem+=1
if dem==0:
    print("No found")
    
    
    
    

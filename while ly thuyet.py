#bài tập nhập điểm học
while True:
    hten=input("Nhập tên: ")
    mhoc=input("Nhập môn học: ")
    diem=float(input("Nhập điểm: "))
    print(f"Học sinh {hten},môn học {mhoc}, có số điểm {diem}")
    if diem >= 7:
        print("xếp loại đạt")
    else:
        print("KHÔNG ĐẠT")
    hoi=input("Ấn phím N để thoát hoặc chọn ký tự khác để tiếp")
    if hoi=="N":
        break
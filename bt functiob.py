class Student:
    def __init__(self,ho, ten, tuoi, diem):
        self.ho= ho
        self.ten= ten
        self.tuoi= tuoi
        self.diem= diem
class_01 = [
    Student("Nguyen", "Van A", 20, 8.5),
    Student("Tran", "Thi B", 22, 9.0),
    Student("Le", "Tuan C", 21, 7.5),
    Student("Pham", "Hong D", 19, 8.0)
]
class_02 = [
    Student("Hoang", "Quoc E", 23, 8.0),
    Student("Vo", "Thanh F", 20, 9.5),
    Student("Duong", "Hoa G", 22, 7.0),
    Student("Ngo", "Minh H", 21, 8.5)
]
print("Số lượng lớp 01: ", len(class_01))
print("Số lượng lớp 02: ", len(class_02))
diem_trung_binh_class_01=sum(student.diem for student in class_01)/ len(class_01)
diem_trung_binh_class_02=sum(student.diem for student in class_02)/ len(class_02)
print("điểm trung bình của lớp 01 là: ", diem_trung_binh_class_01)
print("diểm trung bình của lớp 02 là: ", diem_trung_binh_class_02)
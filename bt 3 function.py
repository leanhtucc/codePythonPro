
danh_sach_lop = {
    "Lớp A": {
        "sv1": 8.5,
        "sv2": 7.9,
        "sv3": 9.1
    },
    "Lớp B": {
        "sv1": 7.2,
        "sv2": 6.8,
        "sv3": 8.3
    },
    "Lớp C": {
        "sv1": 9.7,
        "sv2": 8.9,
        "sv3": 9.5
    }
}
diem_cao_nhat = {}
for lop, danh_sach_sv in danh_sach_lop.items():
    diem_cao_nhat[lop] = max(danh_sach_sv.values())
diem_trung_binh = {}
for lop, danh_sach_sv in danh_sach_lop.items():
    diem_trung_binh[lop] = sum(danh_sach_sv.values()) / len(danh_sach_sv)
for lop, diem in diem_cao_nhat.items():
    print("Sinh viên điểm cao nhất lớp", lop, "có điểm là:", diem)

for lop, diem in diem_trung_binh.items():
    print("Điểm trung bình của lớp", lop, "là:", diem)

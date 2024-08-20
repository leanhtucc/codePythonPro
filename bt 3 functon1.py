# Danh sách các từ điển chứa thông tin sinh viên
students_data = [
    {'ma_sv': 'SV001', 'lop': 'A', 'diem': 8.5},
    {'ma_sv': 'SV002', 'lop': 'A', 'diem': 7.5},
    {'ma_sv': 'SV003', 'lop': 'B', 'diem': 9.0},
    {'ma_sv': 'SV004', 'lop': 'B', 'diem': 8.0},
    # Thêm các sinh viên khác vào đây
]

# Tạo một từ điển để lưu thông tin sinh viên điểm cao nhất mỗi lớp
highest_scores = {}
medium_score ={}
total_score=0
# Tính điểm trung bình mỗi lớp và in ra sinh viên điểm cao nhất mỗi lớp
for student in students_data:
    ma_sv = student['ma_sv']
    lop = student['lop']
    diem = student['diem']

    # Kiểm tra xem có thông tin lớp trong từ điển chưa
    if lop not in highest_scores:
        highest_scores[lop] = {'ma_sv': ma_sv, 'diem': diem}
    else:
        # So sánh điểm và cập nhật nếu có sinh viên có điểm cao hơn
        if diem > highest_scores[lop]['diem']:
            highest_scores[lop] = {'ma_sv': ma_sv, 'diem': diem}

# In ra sinh viên điểm cao nhất mỗi lớp
for lop, info in highest_scores.items():
    print(f'Lớp {lop}: Sinh viên {info["ma_sv"]} có điểm cao nhất với điểm {info["diem"]}')

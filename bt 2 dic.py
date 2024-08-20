def in_danh_sach_nguoi(danh_sach):
    print("Danh sách người trong từ điển:")
    for nguoi in danh_sach.keys():
        print(nguoi)


def in_danh_sach_mon_the_thao(danh_sach):
    print("Danh sách các môn thể thao trong từ điển:")
    for mon_the_thao in danh_sach.values():
        print(mon_the_thao)


def mon_nhieu_nguoi_yeu_thich(nhom_nguoi):
    mon_the_thao_count = {}
    max_count = 0
    for mon_the_thao in nhom_nguoi.values():
        if mon_the_thao in mon_the_thao_count:
            mon_the_thao_count[mon_the_thao] += 1
        else:
            mon_the_thao_count[mon_the_thao] = 1
        if mon_the_thao_count[mon_the_thao] > max_count:
            max_count = mon_the_thao_count[mon_the_thao]

    nguoi_nhieu_yeu_thich = []
    for nguoi, mon_the_thao in nhom_nguoi.items():
        if mon_the_thao_count[mon_the_thao] == max_count:
            nguoi_nhieu_yeu_thich.append(nguoi)

    return (max_count, nguoi_nhieu_yeu_thich)


# Khởi tạo từ điển chứa thông tin của N người bạn và môn thể thao yêu thích
nhom_nguoi = {
    "A": "soccer",
    "B": "badminton",
    "C": "soccer",
    "D": "basketball",
    "E": "badminton"
}

# In ra danh sách người trong từ điển
in_danh_sach_nguoi(nhom_nguoi)
print()

# In ra danh sách các môn thể thao trong từ điển
in_danh_sach_mon_the_thao(nhom_nguoi)
print()

# In ra môn thể thao có nhiều người yêu thích nhất và danh sách những người đó
max_count, nguoi_nhieu_yeu_thich = mon_nhieu_nguoi_yeu_thich(nhom_nguoi)
print(f"Môn thể thao có nhiều người yêu thích nhất ({max_count} người):")
for nguoi in nguoi_nhieu_yeu_thich:
    print(nguoi)

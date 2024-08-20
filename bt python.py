

#bài 2
nhom_nguoi={
      "A": "soccer",
      "B": "badminton",
      "C": "soccer",
      "D": "Basketball",
}
def in_danh_sach_nguoi(danh_sach):
    print("In danh sách người trong từ điển: ")
    for nguoi in danh_sach.keys():
        print(nguoi)
def in_danh_sach_cac_mon_the_thao(danh_sach):
    print("In danh sách các môn thể thao: ")
    for mon_the_thao in danh_sach.values():
        print(mon_the_thao)
def in_cac_mon_the_thao_yeu_thich(nhom_nguoi):
    mon_the_thao_count= {}
    max_count=0
    for mon_the_thao in nhom_nguoi.values():
        if mon_the_thao in mon_the_thao_count:
            mon_the_thao_count[mon_the_thao]+=1
        else:
            mon_the_thao_count[mon_the_thao]=1
            if mon_the_thao_count[mon_the_thao]> max_count:
                max_count=mon_the_thao_count[mon_the_thao]
    nguoi_yeu_thich = []
    for nguoi,mon_the_thao in nhom_nguoi.items():
        if mon_the_thao_count[mon_the_thao]==max_count:
            nguoi_yeu_thich.append(nguoi)
    return(max_count, nguoi_yeu_thich)

in_danh_sach_nguoi(nhom_nguoi)
print()
in_danh_sach_cac_mon_the_thao(nhom_nguoi)
print()
max_count, nguoi_yeu_thich = in_cac_mon_the_thao_yeu_thich(nhom_nguoi)
print(f"Môn thể thao nhiều người yêu thích có {max_count} người")
for nguoi in nguoi_yeu_thich:
    print(nguoi)
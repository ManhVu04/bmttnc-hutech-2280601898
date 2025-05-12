so_h_lam = float(input("Nhập số h làm việc hàng tuần: "))
muc_luong_tieu_chuan = float(input("Nhập mức lương tiêu chuẩn: "))

gio_tieu_chuan = 44

gio_vuot_chuan = max(0, so_h_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * muc_luong_tieu_chuan + gio_vuot_chuan * muc_luong_tieu_chuan * 1.5
print("Thực lĩnh là: ", thuc_linh)

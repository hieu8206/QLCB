from tkinter import messagebox
from models import QLCB, CongNhan, KySu, NhanVien

qlcb = QLCB()

def them_cb(loai, ho_ten, tuoi, gioi_tinh, dia_chi, thong_tin, refresh_func):
    # Kiểm tra dữ liệu đầu vào
    if not all([ho_ten, tuoi, gioi_tinh, dia_chi, thong_tin]):
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin.")
        return

    try:
        tuoi = int(tuoi)
    except ValueError:
        messagebox.showwarning("Sai định dạng", "Tuổi phải là số nguyên.")
        return
    
    # Tạo đối tượng tương ứng
    if loai == "Công Nhân":
        cb = CongNhan(ho_ten, tuoi, gioi_tinh, dia_chi, thong_tin)
    elif loai == "Kỹ Sư":
        cb = KySu(ho_ten, tuoi, gioi_tinh, dia_chi, thong_tin)
    elif loai == "Nhân Viên":
        cb = NhanVien(ho_ten, tuoi, gioi_tinh, dia_chi, thong_tin)
    else:
        messagebox.showerror("Lỗi", "Loại cán bộ không hợp lệ.")
        return
    
    # Thêm vào hệ thống và cập nhật giao diện
    qlcb.them_can_bo(cb)
    refresh_func()

def tim_cb(ten, listbox):
    ket_qua = qlcb.tim_kiem_theo_ten(ten)
    listbox.delete(0, "end")
    for cb in ket_qua:
        listbox.insert("end", str(cb))

def xoa_cb(ho_ten, refresh_func):
    if not ho_ten:
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập họ tên để xóa.")
        return
    qlcb.xoa_can_bo(ho_ten)
    refresh_func()

def cap_nhat_cb(loai, ho_ten, tuoi, gioi_tinh, dia_chi, thong_tin, refresh_func):
    ho_ten_cu = ho_ten

    try:
        tuoi = int(tuoi)
    except ValueError:
        messagebox.showwarning("Sai định dạng", "Tuổi phải là số.")
        return

    if loai == "Công Nhân":
        cb = CongNhan(ho_ten, tuoi, gioi_tinh, dia_chi, thong_tin)
    elif loai == "Kỹ Sư":
        cb = KySu(ho_ten, tuoi, gioi_tinh, dia_chi, thong_tin)
    elif loai == "Nhân Viên":
        cb = NhanVien(ho_ten, tuoi, gioi_tinh, dia_chi, thong_tin)
    else:
        messagebox.showerror("Lỗi", "Loại cán bộ không hợp lệ.")
        return

    ok = qlcb.cap_nhat_can_bo(ho_ten_cu, cb)
    if not ok:
        messagebox.showinfo("Không tìm thấy", "Không tìm thấy cán bộ để cập nhật.")
    refresh_func()

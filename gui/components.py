import tkinter as tk
from tkinter import ttk
from . import handlers

def setup_gui():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Quản Lý Cán Bộ")
    
    # Tạo Frame chứa các widget nhập liệu
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)# cách lề 10px xung quanh frame
    
    # Tạo các label cho cho form nhập liệu
    tk.Label(frame, text="Họ tên").grid(row=0, column=0)
    tk.Label(frame, text="Tuổi").grid(row=1, column=0)
    tk.Label(frame, text="Giới tính").grid(row=2, column=0)
    tk.Label(frame, text="Địa chỉ").grid(row=3, column=0)
    tk.Label(frame, text="Loại cán bộ").grid(row=4, column=0)
    tk.Label(frame, text="Thông tin riêng").grid(row=5, column=0)
    
    # Tạo các widget nhập liệu
    ho_ten_entry = tk.Entry(frame)
    tuoi_entry = tk.Entry(frame)
    gioi_tinh_entry = tk.Entry(frame)
    dia_chi_entry = tk.Entry(frame)
    
    # Combobox chọn loại cán bộ
    loai_var = tk.StringVar(value="Công Nhân")
    loai_cb = ttk.Combobox(frame, textvariable=loai_var, values=["Công Nhân", "Kỹ Sư", "Nhân Viên"], state="readonly")
    thong_tin_entry = tk.Entry(frame)
    
    # Vị trí các widget 
    ho_ten_entry.grid(row=0, column=1)
    tuoi_entry.grid(row=1, column=1)
    gioi_tinh_entry.grid(row=2, column=1)
    dia_chi_entry.grid(row=3, column=1)
    loai_cb.grid(row=4, column=1)
    thong_tin_entry.grid(row=5, column=1)
    
    # Hiển thị danh sách cán bộ   
    listbox = tk.Listbox(root, width=100)
    listbox.pack(padx=10, pady=10) # Cách lề 10px xung quanh listbox
    
    # Làm mới danh sách
    def refresh_listbox():
        listbox.delete(0, tk.END)
        for cb in handlers.qlcb.danh_sach:
            listbox.insert(tk.END, str(cb))
            
    # Tạo các nút chức năng và gán handlers        

    tk.Button(frame, text="Thêm", command=lambda: handlers.them_cb(loai_var.get(), ho_ten_entry.get(), tuoi_entry.get(),
                                                                    gioi_tinh_entry.get(), dia_chi_entry.get(),
                                                                    thong_tin_entry.get(), refresh_listbox)).grid(row=6, column=0)

    tk.Button(frame, text="Cập nhật", command=lambda: handlers.cap_nhat_cb(loai_var.get(), ho_ten_entry.get(), tuoi_entry.get(),
                                                                           gioi_tinh_entry.get(), dia_chi_entry.get(),
                                                                           thong_tin_entry.get(), refresh_listbox)).grid(row=6, column=1)

    tk.Button(frame, text="Xóa", command=lambda: handlers.xoa_cb(ho_ten_entry.get(), refresh_listbox)).grid(row=7, column=0)
    
    # Chức năng tìm kiếm
    tk.Label(frame, text="Tìm theo tên:").grid(row=8, column=0)
    tim_entry = tk.Entry(frame)
    tim_entry.grid(row=8, column=1)
    tk.Button(frame, text="Tìm", command=lambda: handlers.tim_cb(tim_entry.get(), listbox)).grid(row=8, column=2)

    refresh_listbox()
    root.mainloop()

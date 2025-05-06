import json
import os

# Lớp cơ sở CanBo sử dụng ABSTRACTION
class CanBo:
    # ENCAPSULATION - sử dụng property để đóng gói các thuộc tính
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self._ho_ten = ho_ten
        self._tuoi = tuoi
        self._gioi_tinh = gioi_tinh
        self._dia_chi = dia_chi

    @property
    def ho_ten(self):
        return self._ho_ten

    @ho_ten.setter
    def ho_ten(self, value):
        self._ho_ten = value

    @property
    def tuoi(self):
        return self._tuoi

    @tuoi.setter
    def tuoi(self, value):
        self._tuoi = value

    @property
    def gioi_tinh(self):
        return self._gioi_tinh

    @gioi_tinh.setter
    def gioi_tinh(self, value):
        self._gioi_tinh = value

    @property
    def dia_chi(self):
        return self._dia_chi

    @dia_chi.setter
    def dia_chi(self, value):
        self._dia_chi = value

    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    def __str__(self):
        return f"Họ và tên: {self.ho_ten}, Tuổi: {self.tuoi}, Giới tính: {self.gioi_tinh}, Địa chỉ: {self.dia_chi}"

    def to_dict(self):
        return {
            'ho_ten': self.ho_ten,
            'tuoi': self.tuoi,
            'gioi_tinh': self.gioi_tinh,
            'dia_chi': self.dia_chi,
            'loai': self.__class__.__name__.lower()
        }

# Lớp CongNhan kế thừa từ lớp CanBo
class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac

    def __str__(self):
        return f"[Công Nhân] {super().__str__()}, Bậc: {self.bac}"

    def to_dict(self):
        data = super().to_dict()
        data['bac'] = self.bac
        return data

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def __str__(self):
        return f"[Kỹ Sư] {super().__str__()}, Ngành đào tạo: {self.nganh_dao_tao}"

    def to_dict(self):
        data = super().to_dict()
        data['nganh_dao_tao'] = self.nganh_dao_tao
        return data

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def __str__(self):
        return f"[Nhân Viên] {super().__str__()}, Công việc: {self.cong_viec}"

    def to_dict(self):
        data = super().to_dict()
        data['cong_viec'] = self.cong_viec
        return data

class QLCB:
    DATA_FILE = 'data.json'
    
    def __init__(self):
        self.danh_sach = []
        self.load_data()

    def them_can_bo(self, can_bo):
        self.danh_sach.append(can_bo)
        self.save_data()

    def tim_kiem_theo_ten(self, ten):
        return [cb for cb in self.danh_sach if ten.lower() in cb.ho_ten.lower()]

    def save_data(self):
        data = [self.can_bo_to_dict(cb) for cb in self.danh_sach]
        with open(self.DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_data(self):
        if not os.path.exists(self.DATA_FILE):
            return
            
        with open(self.DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for item in data:
            if item['loai'] == 'congnhan':
                cb = CongNhan(item['ho_ten'], item['tuoi'], item['gioi_tinh'], item['dia_chi'], item['bac'])
            elif item['loai'] == 'kysu':
                cb = KySu(item['ho_ten'], item['tuoi'], item['gioi_tinh'], item['dia_chi'], item['nganh_dao_tao'])
            elif item['loai'] == 'nhanvien':
                cb = NhanVien(item['ho_ten'], item['tuoi'], item['gioi_tinh'], item['dia_chi'], item['cong_viec'])
            else:
                cb = CanBo(item['ho_ten'], item['tuoi'], item['gioi_tinh'], item['dia_chi'])
            self.danh_sach.append(cb)

    def can_bo_to_dict(self, can_bo):
        return can_bo.to_dict()
    
    def xoa_can_bo(self, ho_ten):
        self.danh_sach = [cb for cb in self.danh_sach if cb.ho_ten != ho_ten]
        self.save_data()
        return len(self.danh_sach)
    
    def lay_can_bo_theo_ten(self, ho_ten):
        for cb in self.danh_sach:
            if cb.ho_ten == ho_ten:
                return cb
        return None
    
    def cap_nhat_can_bo(self, ho_ten_cu, can_bo_moi):
        for i, cb in enumerate(self.danh_sach):
            if cb.ho_ten == ho_ten_cu:
                self.danh_sach[i] = can_bo_moi
                self.save_data()
                return True
        return False
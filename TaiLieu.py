class TaiLieu:
    def __init__(self, ma_tai_lieu, ten_nha_xuat_ban, so_ban_phat_hanh):
        self._ma_tai_lieu = ma_tai_lieu
        self._ten_nha_xuat_ban = ten_nha_xuat_ban
        self._so_ban_phat_hanh = so_ban_phat_hanh
    
    def get_ma_tai_lieu(self):
        return self._ma_tai_lieu
    
    def get_ten_nha_xuat_ban(self):
        return self._ten_nha_xuat_ban
    
    def set_ten_nha_xuat_ban(self, ten_moi):
        if not ten_moi:
            raise ValueError("Tên nhà xuất bản không được để trống")
        self._ten_nha_xuat_ban = ten_moi
    
    def get_so_ban_phat_hanh(self):
        return self._so_ban_phat_hanh
    
    def set_so_ban_phat_hanh(self, so_ban_moi):
        if so_ban_moi < 0:
            raise ValueError("Số bản phát hành không được âm")
        self._so_ban_phat_hanh = so_ban_moi
    
    def hien_thi_thong_tin(self):
        raise NotImplementedError("Lớp con phải triển khai phương thức này.")
    
    def get_loai(cls):
        return cls.__name__
    get_loai = classmethod(get_loai)

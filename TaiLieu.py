class TaiLieu:
    def __init__(self, ma_tai_lieu, ten_nha_xuat_ban, so_ban_phat_hanh):
        self._ma_tai_lieu = ma_tai_lieu # Mã tài liệu
        self.set_ten_nha_xuat_ban(ten_nha_xuat_ban) # Gọi setter gán tên nhà xuất bản
        self.set_so_ban_phat_hanh(so_ban_phat_hanh) # Gọi setter gán số bản phát hành
    
    def get_ma_tai_lieu(self): # getter cho mã tài liệu
        return self._ma_tai_lieu
    
    def get_ten_nha_xuat_ban(self): # getter cho tên nhà xuất bản
        return self._ten_nha_xuat_ban
    
    def set_ten_nha_xuat_ban(self, ten_moi): # setter cho tên nhà xuất bản
        if not ten_moi:
            raise ValueError("Tên nhà xuất bản không được để trống.") # Hiển thị lỗi nếu người dùng ko nhập tên nhà xuất bản
        self._ten_nha_xuat_ban = ten_moi
    
    def get_so_ban_phat_hanh(self): # getter cho số bản phát hành
        return self._so_ban_phat_hanh
    
    def set_so_ban_phat_hanh(self, so_ban_moi): # setter cho số bản phát hành
        if so_ban_moi < 0:
            raise ValueError("Số bản phát hành không được âm.") # Hiển thị lỗi người dùng nhập số không phù hợp
        self._so_ban_phat_hanh = so_ban_moi
    
    def hien_thi_thong_tin(self):
        raise NotImplementedError("Lớp con phải triển khai phương thức này.") # Phương thức bắt buộc lớp con phải triển khai (để tránh lỗi lớp con ko triển khai hiển thị thông tin)
    
    def get_loai(cls):
        return cls.__name__ # Trả về tên lớp ("Sach", "TapChi", "Bao")
    get_loai = classmethod(get_loai) # Biến phương thức thành classmethod để gọi từ đối tượng hoặc lớp đều được

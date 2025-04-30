from TaiLieu import TaiLieu

class TapChi(TaiLieu):
    def __init__(self, ma_tai_lieu, ten_nha_xuat_ban, so_ban_phat_hanh, so_phat_hanh, thang_phat_hanh):
        super().__init__(ma_tai_lieu, ten_nha_xuat_ban, so_ban_phat_hanh) # Gọi constructor (hàm khởi tạo) lớp mẹ
        self.set_so_phat_hanh(so_phat_hanh) # setter gán số phát hành
        self.set_thang_phat_hanh(thang_phat_hanh) # setter gán số phát hành

    def get_so_phat_hanh(self): # getter gán số phát hành
        return self._so_phat_hanh

    def set_so_phat_hanh(self, value): # setter gắn số phát hành
        if value <= 0:
            raise ValueError("Số phát hành phải lớn hơn 0.") # Hiển thị lỗi nếu người dùng nhập số phát hành <= 0
        self._so_phat_hanh = value # Gán value hợp lệ

    def get_thang_phat_hanh(self): # getter tháng phát hành
        return self._thang_phat_hanh

    def set_thang_phat_hanh(self, value):
        if not 1 <= value <= 12:
            raise ValueError("Tháng phát hành phải từ 1 đến 12.") # Hiển thị lỗi nếu người dùng nhập tháng ko hợp lệ
        self._thang_phat_hanh = value # Gán value hợp lệ

    def hien_thi_thong_tin(self): # Hiển thị thông tin
        print(f"Mã tài liệu: {self.get_ma_tai_lieu()}")
        print(f"Nhà xuất bản: {self.get_ten_nha_xuat_ban()}")
        print(f"Số bản phát hành: {self.get_so_ban_phat_hanh()}")
        print(f"Loại tài liệu: {self.get_loai()}")
        print(f"Số phát hành: {self.get_so_phat_hanh()}")
        print(f"Tháng phát hành: {self.get_thang_phat_hanh()}")

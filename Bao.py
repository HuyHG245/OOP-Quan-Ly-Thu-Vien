from TaiLieu import TaiLieu
from datetime import datetime

class Bao(TaiLieu):
    def __init__(self, ma_tai_lieu, ten_nha_xuat_ban, so_ban_phat_hanh, ngay_phat_hanh):
        super().__init__(ma_tai_lieu, ten_nha_xuat_ban, so_ban_phat_hanh) # Gọi hàm khởi tạo lớp mẹ 
        self._ngay_phat_hanh = ngay_phat_hanh

    def get_ngay_phat_hanh(self):
        return self._ngay_phat_hanh

    def set_ngay_phat_hanh(self, value):
        try:
            datetime.strptime(value, "%d/%m/%Y")
            self._ngay_phat_hanh = value
        except ValueError:
            raise ValueError("Ngày phát hành phải có định dạng DD/MM/YYYY")

    def hien_thi_thong_tin(self):
        print(f"Mã tài liệu: {self.get_ma_tai_lieu()}")
        print(f"Nhà xuất bản: {self.get_ten_nha_xuat_ban()}")
        print(f"Số bản phát hành: {self.get_so_ban_phat_hanh()}")
        print(f"Loại tài liệu: {self.get_loai()}")
        print(f"Ngày phát hành: {self.get_ngay_phat_hanh()}")
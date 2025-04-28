from TaiLieu import TaiLieu

class Sach(TaiLieu):
    def __init__(self, ma_tai_lieu, ten_nha_xuat_ban, so_ban_phat_hanh, ten_tac_gia, so_trang):
        super().__init__(ma_tai_lieu, ten_nha_xuat_ban, so_ban_phat_hanh) # Gọi hàm khởi tạo lớp mẹ
        self._ten_tac_gia = ten_tac_gia
        self._so_trang = so_trang

    def get_ten_tac_gia(self):
        return self._ten_tac_gia

    def set_ten_tac_gia(self, value):
        if not value:
            raise ValueError("Tên tác giả không được để trống")
        self._ten_tac_gia = value

    def get_so_trang(self):
        return self._so_trang

    def set_so_trang(self, value):
        if value <= 0:
            raise ValueError("Số trang phải lớn hơn 0")
        self._so_trang = value

    def hien_thi_thong_tin(self):
        print(f"Mã tài liệu: {self.get_ma_tai_lieu()}")
        print(f"Nhà xuất bản: {self.get_ten_nha_xuat_ban()}")
        print(f"Số bản phát hành: {self.get_so_ban_phat_hanh()}")
        print(f"Loại tài liệu: {self.get_loai()}")
        print(f"Tên tác giả: {self.get_ten_tac_gia()}")
        print(f"Số trang: {self.get_so_trang()}")
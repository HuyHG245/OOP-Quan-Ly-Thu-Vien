from TaiLieu import TaiLieu

class QuanLySach:
    def __init__(self):
        self._danh_sach_tai_lieu = [] # Danh sách tài liệu được lưu trong một mảng
    
    def them_tai_lieu(self, tai_lieu): # Thêm tài liệu mới vào danh sách
        if not isinstance(tai_lieu, TaiLieu): # Kiểm tra đầu vào phải là đối tượng TaiLieu
            raise ValueError("Chỉ chấp nhận tài liệu hợp lệ.")
        
        # Kiểm tra trùng mã tài liệu
        for tl in self._danh_sach_tai_lieu:
            if tl.get_ma_tai_lieu() == tai_lieu.get_ma_tai_lieu():
                raise ValueError("Mã tài liệu đã tồn tại.")
        
        # Thêm vào danh sách
        self._danh_sach_tai_lieu.append(tai_lieu)
        print("Thêm tài liệu thành công.")
    
    def xoa_tai_lieu(self, ma_tai_lieu): # Xóa tài liệu theo mã
        for i, tl in enumerate(self._danh_sach_tai_lieu): # Duyệt qua danh sách để tìm
            if tl.get_ma_tai_lieu() == ma_tai_lieu: # Xóa khỏi danh sách nếu tìm thấy mã
                del self._danh_sach_tai_lieu[i]
                print("Xóa thành công.")
                return True
        print("Không tìm thấy tài liệu.")
        return False
    
    def hien_thi_danh_sach(self): # Hiển thị toàn bộ danh sách
        if not self._danh_sach_tai_lieu:
            print("Danh sách trống.")
            return
        
        print("\nDANH SÁCH TÀI LIỆU")
        for tai_lieu in self._danh_sach_tai_lieu:
            tai_lieu.hien_thi_thong_tin() # Gọi phương thức hiển thị của từng tài liệu
    
    def tim_kiem_theo_loai(self, loai): # Tìm kiếm theo loại tài liệu
        ket_qua = []
        for tl in self._danh_sach_tai_lieu:
            if tl.get_loai().lower() == loai.lower(): # So sánh tên class với loại cần tìm
                ket_qua.append(tl)
        
        if not ket_qua:
            print(f"Không tìm thấy {loai}")
            return
        
        print(f"\nKẾT QUẢ TÌM KIẾM {loai.upper()}")
        for tl in ket_qua:
            tl.hien_thi_thong_tin() # Hiển thị kết quả tìm kiếm

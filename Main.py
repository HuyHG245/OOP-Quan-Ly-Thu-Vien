from QuanLySach import QuanLySach
from Sach import Sach
from TapChi import TapChi
from Bao import Bao
from datetime import datetime

def main():
    ql = QuanLySach() # Khởi tạo hệ thống quản lý
    
    while True: # Vòng lặp Menu
        print("\nHỆ THỐNG QUẢN LÝ THƯ VIỆN")
        print("1. Thêm tài liệu")
        print("2. Xóa tài liệu")
        print("3. Hiển thị danh sách")
        print("4. Tìm kiếm theo loại")
        print("5. Thoát")
        
        choice = input("Chọn chức năng: ") # Người dùng nhập lựa chọn từ 1-5 
        
        if choice == "1":
            them_tai_lieu(ql) # Gọi hàm thêm tài liệu
        elif choice == "2":
            ma = input("Nhập mã tài liệu cần xóa: ") # Nhập mã xóa tài liệu
            ql.xoa_tai_lieu(ma)
        elif choice == "3":
            ql.hien_thi_danh_sach() # Hiển thị toàn bộ danh sách
        elif choice == "4":
            loai = input("Nhập loại cần tìm (Sach/TapChi/Bao): ") # Tìm kiếm theo loại được nhập
            ql.tim_kiem_theo_loai(loai)
        elif choice == "5":
            print("Thao tác hoàn tất.")
            break # Kết thúc chương trình
        else:
            print("Lựa chọn không hợp lệ.") # Lựa chọn nằm ngoài các lựa chọn đã được đề ra

def them_tai_lieu(ql): # Hàm thêm tài liệu
    print("\nChọn loại tài liệu:")
    print("1. Sách")
    print("2. Tạp chí")
    print("3. Báo")
    
    loai = input("Chọn loại (1-3): ") # Chọn loại tài liệu muốn thêm
    
    # Nhập thông tin chung
    ma = input("Mã tài liệu: ")
    ten_nxb = input("Tên NXB: ")
    so_ban = int(input("Số bản phát hành: "))
    
    try:
        if loai == "1":
            # Nhập thông tin riêng của Sách
            tac_gia = input("Tác giả: ")
            so_trang = int(input("Số trang: "))
            ql.them_tai_lieu(Sach(ma, ten_nxb, so_ban, tac_gia, so_trang))
        elif loai == "2":
            # Nhập thông tin riêng của Tạp chí
            so_ph = int(input("Số phát hành: "))
            thang_ph = int(input("Tháng phát hành: "))
            ql.them_tai_lieu(TapChi(ma, ten_nxb, so_ban, so_ph, thang_ph))
        elif loai == "3":
            # Nhập thông tin riêng của Báo
            ngay_ph = input("Ngày phát hành (dd/mm/yyyy): ")
            ngay_ph = datetime.strptime(ngay_ph, "%d/%m/%Y") # Chuyển thành đối tượng datetime
            ql.them_tai_lieu(Bao(ma, ten_nxb, so_ban, ngay_ph))
        else:
            print("Loại không hợp lệ.") # Lựa chọn sai
    except ValueError as e:
        print(f"Lỗi: {e}") # Hiển thị người dùng nhập sai

if __name__ == "__main__":
    main() # Chạy file

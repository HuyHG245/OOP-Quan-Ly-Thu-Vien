from tkinter import *
from tkinter import ttk, messagebox
from QuanLySach import QuanLySach
from Sach import Sach
from TapChi import TapChi
from Bao import Bao
from datetime import datetime

class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý thư viện")
        self.root.geometry("800x600")
        
        self.ql = QuanLySach()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Tạo notebook (tab)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=BOTH, expand=True)
        
        # Tab thêm tài liệu
        self.tab_add = Frame(self.notebook)
        self.notebook.add(self.tab_add, text="Thêm tài liệu")
        self.create_add_tab()
        
        # Tab xóa tài liệu
        self.tab_delete = Frame(self.notebook)
        self.notebook.add(self.tab_delete, text="Xóa tài liệu")
        self.create_delete_tab()
        
        # Tab hiển thị danh sách
        self.tab_display = Frame(self.notebook)
        self.notebook.add(self.tab_display, text="Danh sách tài liệu")
        self.create_display_tab()
        
        # Tab tìm kiếm
        self.tab_search = Frame(self.notebook)
        self.notebook.add(self.tab_search, text="Tìm kiếm")
        self.create_search_tab()
    
    def create_add_tab(self):
        # Frame chứa các widget
        frame = LabelFrame(self.tab_add, text="Thông tin tài liệu", padx=10, pady=10)
        frame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        
        # Combobox chọn loại tài liệu
        Label(frame, text="Loại tài liệu:").grid(row=0, column=0, sticky=W, pady=5)
        self.doc_type = StringVar()
        self.type_combobox = ttk.Combobox(frame, textvariable=self.doc_type, 
                                        values=["Sách", "Tạp chí", "Báo"], state="readonly")
        self.type_combobox.grid(row=0, column=1, sticky=EW, pady=5)
        self.type_combobox.bind("<<ComboboxSelected>>", self.update_fields)
        
        # Thông tin chung
        Label(frame, text="Mã tài liệu:").grid(row=1, column=0, sticky=W, pady=5)
        self.ma_tai_lieu = Entry(frame)
        self.ma_tai_lieu.grid(row=1, column=1, sticky=EW, pady=5)
        
        Label(frame, text="Tên NXB:").grid(row=2, column=0, sticky=W, pady=5)
        self.ten_nxb = Entry(frame)
        self.ten_nxb.grid(row=2, column=1, sticky=EW, pady=5)
        
        Label(frame, text="Số bản phát hành:").grid(row=3, column=0, sticky=W, pady=5)
        self.so_ban = Entry(frame)
        self.so_ban.grid(row=3, column=1, sticky=EW, pady=5)
        
        # Frame cho thông tin riêng (sẽ thay đổi theo loại tài liệu)
        self.specific_frame = Frame(frame)
        self.specific_frame.grid(row=4, column=0, columnspan=2, sticky=EW, pady=10)
        
        # Nút thêm
        Button(frame, text="Thêm tài liệu", command=self.them_tai_lieu).grid(row=5, column=0, columnspan=2, pady=10)
    
    def update_fields(self, event=None):
        # Xóa các widget cũ trong specific_frame
        for widget in self.specific_frame.winfo_children():
            widget.destroy()
        
        doc_type = self.doc_type.get()
        
        if doc_type == "Sách":
            Label(self.specific_frame, text="Tác giả:").grid(row=0, column=0, sticky=W, pady=5)
            self.tac_gia = Entry(self.specific_frame)
            self.tac_gia.grid(row=0, column=1, sticky=EW, pady=5)
            
            Label(self.specific_frame, text="Số trang:").grid(row=1, column=0, sticky=W, pady=5)
            self.so_trang = Entry(self.specific_frame)
            self.so_trang.grid(row=1, column=1, sticky=EW, pady=5)
        
        elif doc_type == "Tạp chí":
            Label(self.specific_frame, text="Số phát hành:").grid(row=0, column=0, sticky=W, pady=5)
            self.so_ph = Entry(self.specific_frame)
            self.so_ph.grid(row=0, column=1, sticky=EW, pady=5)
            
            Label(self.specific_frame, text="Tháng phát hành:").grid(row=1, column=0, sticky=W, pady=5)
            self.thang_ph = Entry(self.specific_frame)
            self.thang_ph.grid(row=1, column=1, sticky=EW, pady=5)
        
        elif doc_type == "Báo":
            Label(self.specific_frame, text="Ngày phát hành (dd/mm/yyyy):").grid(row=0, column=0, sticky=W, pady=5)
            self.ngay_ph = Entry(self.specific_frame)
            self.ngay_ph.grid(row=0, column=1, sticky=EW, pady=5)
    
    def them_tai_lieu(self):
        try:
            ma = self.ma_tai_lieu.get()
            ten_nxb = self.ten_nxb.get()
            so_ban = int(self.so_ban.get())
            doc_type = self.doc_type.get()
            
            if doc_type == "Sách":
                tac_gia = self.tac_gia.get()
                so_trang = int(self.so_trang.get())
                self.ql.them_tai_lieu(Sach(ma, ten_nxb, so_ban, tac_gia, so_trang))
                messagebox.showinfo("Thành công", "Thêm sách thành công!")
            
            elif doc_type == "Tạp chí":
                so_ph = int(self.so_ph.get())
                thang_ph = int(self.thang_ph.get())
                self.ql.them_tai_lieu(TapChi(ma, ten_nxb, so_ban, so_ph, thang_ph))
                messagebox.showinfo("Thành công", "Thêm tạp chí thành công!")
            
            elif doc_type == "Báo":
                ngay_ph = self.ngay_ph.get()
                ngay_ph = datetime.strptime(ngay_ph, "%d/%m/%Y")
                self.ql.them_tai_lieu(Bao(ma, ten_nxb, so_ban, ngay_ph))
                messagebox.showinfo("Thành công", "Thêm báo thành công!")
            
            # Xóa các trường nhập liệu sau khi thêm
            self.clear_fields()
        
        except ValueError as e:
            messagebox.showerror("Lỗi", f"Dữ liệu không hợp lệ: {e}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")
    
    def clear_fields(self):
        self.ma_tai_lieu.delete(0, END)
        self.ten_nxb.delete(0, END)
        self.so_ban.delete(0, END)
        for widget in self.specific_frame.winfo_children():
            if isinstance(widget, Entry):
                widget.delete(0, END)
    
    def create_delete_tab(self):
        frame = LabelFrame(self.tab_delete, text="Xóa tài liệu", padx=10, pady=10)
        frame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        
        Label(frame, text="Mã tài liệu cần xóa:").grid(row=0, column=0, sticky=W, pady=5)
        self.delete_id = Entry(frame)
        self.delete_id.grid(row=0, column=1, sticky=EW, pady=5)
        
        Button(frame, text="Xóa", command=self.xoa_tai_lieu).grid(row=1, column=0, columnspan=2, pady=10)
    
    def xoa_tai_lieu(self):
        ma = self.delete_id.get()
        if not ma:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập mã tài liệu")
            return
        
        if self.ql.xoa_tai_lieu(ma):
            messagebox.showinfo("Thành công", "Xóa tài liệu thành công")
            self.delete_id.delete(0, END)
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy tài liệu")
    
    def create_display_tab(self):
        # Frame chứa Treeview
        frame = Frame(self.tab_display)
        frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Tạo thanh cuộn
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Tạo Treeview
        self.tree = ttk.Treeview(frame, columns=("Mã", "Loại", "NXB", "Số bản", "Chi tiết"), 
                                yscrollcommand=scrollbar.set)
        self.tree.pack(fill=BOTH, expand=True)
        
        # Cấu hình các cột
        self.tree.heading("#0", text="STT")
        self.tree.column("#0", width=50)
        self.tree.heading("Mã", text="Mã tài liệu")
        self.tree.column("Mã", width=100)
        self.tree.heading("Loại", text="Loại")
        self.tree.column("Loại", width=100)
        self.tree.heading("NXB", text="Nhà xuất bản")
        self.tree.column("NXB", width=150)
        self.tree.heading("Số bản", text="Số bản")
        self.tree.column("Số bản", width=80)
        self.tree.heading("Chi tiết", text="Chi tiết")
        self.tree.column("Chi tiết", width=200)
        
        # Kết nối thanh cuộn với Treeview
        scrollbar.config(command=self.tree.yview)
        
        # Nút hiển thị
        Button(self.tab_display, text="Hiển thị danh sách", command=self.hien_thi_danh_sach).pack(pady=10)
    
    def hien_thi_danh_sach(self):
        # Xóa dữ liệu cũ trong Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Thêm dữ liệu mới
        for i, tl in enumerate(self.ql._danh_sach_tai_lieu, 1):
            details = ""
            if isinstance(tl, Sach):
                details = f"Tác giả: {tl.get_ten_tac_gia()}, Số trang: {tl.get_so_trang()}"
            elif isinstance(tl, TapChi):
                details = f"Số PH: {tl.get_so_phat_hanh()}, Tháng: {tl.get_thang_phat_hanh()}"
            elif isinstance(tl, Bao):
                details = f"Ngày PH: {tl.get_ngay_phat_hanh().strftime('%d/%m/%Y')}"
            
            self.tree.insert("", "end", text=str(i), 
                            values=(tl.get_ma_tai_lieu(), tl.get_loai(), 
                                    tl.get_ten_nha_xuat_ban(), tl.get_so_ban_phat_hanh(), 
                                    details))
    
    def create_search_tab(self):
        frame = LabelFrame(self.tab_search, text="Tìm kiếm tài liệu", padx=10, pady=10)
        frame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        
        Label(frame, text="Loại tài liệu:").grid(row=0, column=0, sticky=W, pady=5)
        self.search_type = StringVar()
        self.search_combobox = ttk.Combobox(frame, textvariable=self.search_type, 
                                          values=["Sách", "Tạp chí", "Báo"], state="readonly")
        self.search_combobox.grid(row=0, column=1, sticky=EW, pady=5)
        
        Button(frame, text="Tìm kiếm", command=self.tim_kiem).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Frame kết quả
        result_frame = Frame(frame)
        result_frame.grid(row=2, column=0, columnspan=2, sticky=EW)
        
        # Treeview hiển thị kết quả
        self.result_tree = ttk.Treeview(result_frame, columns=("Mã", "NXB", "Số bản", "Chi tiết"))
        self.result_tree.pack(fill=BOTH, expand=True)
        
        # Cấu hình các cột
        self.result_tree.heading("#0", text="STT")
        self.result_tree.column("#0", width=50)
        self.result_tree.heading("Mã", text="Mã tài liệu")
        self.result_tree.column("Mã", width=100)
        self.result_tree.heading("NXB", text="Nhà xuất bản")
        self.result_tree.column("NXB", width=150)
        self.result_tree.heading("Số bản", text="Số bản")
        self.result_tree.column("Số bản", width=80)
        self.result_tree.heading("Chi tiết", text="Chi tiết")
        self.result_tree.column("Chi tiết", width=200)
    
    def tim_kiem(self):
        loai_gui = self.search_type.get()
        if not loai_gui:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn loại tài liệu cần tìm")
            return
    
        # Ánh xạ từ tên GUI sang tên class
        loai_map = {
            "Sách": "Sach",
            "Tạp chí": "TapChi",
            "Báo": "Bao"
        }
        loai_can_tim = loai_map.get(loai_gui)
    
        if not loai_can_tim:
            messagebox.showwarning("Cảnh báo", "Loại tài liệu không hợp lệ")
            return
    
        # Xóa dữ liệu cũ trong Treeview
        for item in self.result_tree.get_children():
            self.result_tree.delete(item)
    
        # Thêm dữ liệu mới
        ket_qua = []
        for tl in self.ql._danh_sach_tai_lieu:
            if tl.get_loai() == loai_can_tim:  # So sánh với tên class
                ket_qua.append(tl)
    
        if not ket_qua:
            messagebox.showinfo("Thông báo", f"Không tìm thấy {loai_gui}")
            return
    
        for i, tl in enumerate(ket_qua, 1):
            details = ""
            if isinstance(tl, Sach):
                details = f"Tác giả: {tl.get_ten_tac_gia()}, Số trang: {tl.get_so_trang()}"
            elif isinstance(tl, TapChi):
                details = f"Số PH: {tl.get_so_phat_hanh()}, Tháng: {tl.get_thang_phat_hanh()}"
            elif isinstance(tl, Bao):
                details = f"Ngày PH: {tl.get_ngay_phat_hanh().strftime('%d/%m/%Y')}"
        
            self.result_tree.insert("", "end", text=str(i), 
                values=(tl.get_ma_tai_lieu(), 
                    tl.get_ten_nha_xuat_ban(), 
                    tl.get_so_ban_phat_hanh(), 
                    details))
if __name__ == "__main__":
    root = Tk()
    app = LibraryGUI(root)
    root.mainloop()

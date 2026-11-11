
import tkinter as tk
from tkinter import ttk, messagebox
import csdl_chi_tieu


class UngDungChiTieu(tk.Tk):
    def __init__(self):
        super().__init__()

        # Cấu hình cửa sổ
        self.title("Ứng dụng quản lý chi tiêu")
        self.geometry("1000x650")
        self.resizable(True, True)

        # Tạo bảng dữ liệu nếu chưa tồn tại
        csdl_chi_tieu.tao_bang()

        # Lưu ID giao dịch đang được chọn
        self.id_dang_chon = None

        # ==============================
        # BƯỚC 21: TIÊU ĐỀ
        # ==============================
        self.tieu_de = tk.Label(
            self,
            text="QUẢN LÝ CHI TIÊU CÁ NHÂN",
            font=("Arial", 20, "bold")
        )
        self.tieu_de.pack(pady=15)

        # ==============================
        # BƯỚC 22: KHUNG NHẬP LIỆU
        # ==============================
        self.khung_nhap = tk.LabelFrame(
            self,
            text="Thông tin giao dịch",
            padx=10,
            pady=10
        )
        self.khung_nhap.pack(fill="x", padx=15, pady=5)

        # ==============================
        # BƯỚC 23: CÁC Ô NHẬP LIỆU
        # ==============================
        tk.Label(self.khung_nhap, text="Tên giao dịch:").grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        self.o_ten = tk.Entry(self.khung_nhap, width=25)
        self.o_ten.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.khung_nhap, text="Số tiền:").grid(
            row=0, column=2, padx=5, pady=5, sticky="w"
        )
        self.o_so_tien = tk.Entry(self.khung_nhap, width=20)
        self.o_so_tien.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(self.khung_nhap, text="Loại giao dịch:").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        self.o_loai = ttk.Combobox(
            self.khung_nhap,
            values=["Thu", "Chi"],
            state="readonly",
            width=22
        )
        self.o_loai.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.khung_nhap, text="Danh mục:").grid(
            row=1, column=2, padx=5, pady=5, sticky="w"
        )
        self.o_danh_muc = ttk.Combobox(
            self.khung_nhap,
            values=[
                "Ăn uống",
                "Học tập",
                "Đi lại",
                "Giải trí",
                "Lương",
                "Khác"
            ],
            width=22
        )
        self.o_danh_muc.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(self.khung_nhap, text="Ngày:").grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )
        self.o_ngay = tk.Entry(self.khung_nhap, width=25)
        self.o_ngay.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.khung_nhap, text="Ghi chú:").grid(
            row=2, column=2, padx=5, pady=5, sticky="w"
        )
        self.o_ghi_chu = tk.Entry(self.khung_nhap, width=25)
        self.o_ghi_chu.grid(row=2, column=3, padx=5, pady=5)

        # ==============================
        # BƯỚC 24: CÁC NÚT CHỨC NĂNG
        # ==============================
        self.khung_nut = tk.Frame(self)
        self.khung_nut.pack(pady=10)

        self.nut_them = tk.Button(
            self.khung_nut,
            text="Thêm",
            width=12,
            command=self.them
        )
        self.nut_them.pack(side="left", padx=5)

        self.nut_sua = tk.Button(
            self.khung_nut,
            text="Sửa",
            width=12,
            command=self.sua
        )
        self.nut_sua.pack(side="left", padx=5)

        self.nut_xoa = tk.Button(
            self.khung_nut,
            text="Xóa",
            width=12,
            command=self.xoa
        )
        self.nut_xoa.pack(side="left", padx=5)

        self.nut_lam_moi = tk.Button(
            self.khung_nut,
            text="Làm mới",
            width=12,
            command=self.lam_moi
        )
        self.nut_lam_moi.pack(side="left", padx=5)

        # ==============================
        # BƯỚC 25: BẢNG HIỂN THỊ GIAO DỊCH
        # ==============================
        self.khung_bang = tk.Frame(self)
        self.khung_bang.pack(fill="both", expand=True, padx=15, pady=5)

        cac_cot = (
            "id",
            "ten",
            "so_tien",
            "loai",
            "danh_muc",
            "ngay",
            "ghi_chu"
        )

        self.bang = ttk.Treeview(
            self.khung_bang,
            columns=cac_cot,
            show="headings"
        )

        self.bang.heading("id", text="ID")
        self.bang.heading("ten", text="Tên giao dịch")
        self.bang.heading("so_tien", text="Số tiền")
        self.bang.heading("loai", text="Loại")
        self.bang.heading("danh_muc", text="Danh mục")
        self.bang.heading("ngay", text="Ngày")
        self.bang.heading("ghi_chu", text="Ghi chú")

        self.bang.column("id", width=40, anchor="center")
        self.bang.column("ten", width=150)
        self.bang.column("so_tien", width=100, anchor="center")
        self.bang.column("loai", width=70, anchor="center")
        self.bang.column("danh_muc", width=100, anchor="center")
        self.bang.column("ngay", width=100, anchor="center")
        self.bang.column("ghi_chu", width=150)

        self.bang.pack(fill="both", expand=True)

        # Khi chọn một dòng trong bảng
        self.bang.bind("<<TreeviewSelect>>", self.chon_giao_dich)

        # ==============================
        # BƯỚC 26: KHUNG TÌM KIẾM
        # ==============================
        self.khung_tim_kiem = tk.Frame(self)
        self.khung_tim_kiem.pack(fill="x", padx=15, pady=5)

        tk.Label(
            self.khung_tim_kiem,
            text="Tìm kiếm:"
        ).pack(side="left", padx=5)

        self.o_tim_kiem = tk.Entry(self.khung_tim_kiem, width=30)
        self.o_tim_kiem.pack(side="left", padx=5)

        self.nut_tim_kiem = tk.Button(
            self.khung_tim_kiem,
            text="Tìm",
            command=self.tim_kiem
        )
        self.nut_tim_kiem.pack(side="left", padx=5)

        self.nut_hien_thi_tat_ca = tk.Button(
            self.khung_tim_kiem,
            text="Hiển thị tất cả",
            command=self.hien_thi_giao_dich
        )
        self.nut_hien_thi_tat_ca.pack(side="left", padx=5)

        # ==============================
        # BƯỚC 27: THỐNG KÊ THU CHI
        # ==============================
        self.khung_thong_ke = tk.LabelFrame(
            self,
            text="Thống kê",
            padx=10,
            pady=10
        )
        self.khung_thong_ke.pack(fill="x", padx=15, pady=10)

        self.nhan_tong_thu = tk.Label(
            self.khung_thong_ke,
            text="Tổng thu: 0 VNĐ",
            font=("Arial", 11, "bold")
        )
        self.nhan_tong_thu.pack(side="left", padx=20)

        self.nhan_tong_chi = tk.Label(
            self.khung_thong_ke,
            text="Tổng chi: 0 VNĐ",
            font=("Arial", 11, "bold")
        )
        self.nhan_tong_chi.pack(side="left", padx=20)

        self.nhan_so_du = tk.Label(
            self.khung_thong_ke,
            text="Số dư: 0 VNĐ",
            font=("Arial", 11, "bold")
        )
        self.nhan_so_du.pack(side="left", padx=20)

        # Hiển thị dữ liệu khi mở ứng dụng
        self.hien_thi_giao_dich()

    # ==================================
    # HÀM HIỂN THỊ GIAO DỊCH
    # ==================================
    def hien_thi_giao_dich(self):
        for dong in self.bang.get_children():
            self.bang.delete(dong)

        danh_sach = csdl_chi_tieu.lay_giao_dich()

        for giao_dich in danh_sach:
            self.bang.insert("", "end", values=giao_dich)

        self.cap_nhat_thong_ke(danh_sach)

    # ==================================
    # HÀM CẬP NHẬT THỐNG KÊ
    # ==================================
    def cap_nhat_thong_ke(self, danh_sach):
        tong_thu = 0
        tong_chi = 0

        for giao_dich in danh_sach:
            so_tien = float(giao_dich[2])

            if giao_dich[3] == "Thu":
                tong_thu += so_tien
            elif giao_dich[3] == "Chi":
                tong_chi += so_tien

        so_du = tong_thu - tong_chi

        self.nhan_tong_thu.config(
            text=f"Tổng thu: {tong_thu:,.0f} VNĐ"
        )
        self.nhan_tong_chi.config(
            text=f"Tổng chi: {tong_chi:,.0f} VNĐ"
        )
        self.nhan_so_du.config(
            text=f"Số dư: {so_du:,.0f} VNĐ"
        )

    # ==================================
    # HÀM THÊM GIAO DỊCH
    # ==================================
    def them(self):
        ten = self.o_ten.get().strip()
        so_tien = self.o_so_tien.get().strip()
        loai = self.o_loai.get()
        danh_muc = self.o_danh_muc.get()
        ngay = self.o_ngay.get().strip()
        ghi_chu = self.o_ghi_chu.get().strip()

        if not ten or not so_tien or not loai or not ngay:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập đầy đủ tên, số tiền, loại và ngày!"
            )
            return

        try:
            so_tien = float(so_tien)
            if so_tien <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Lỗi",
                "Số tiền phải là một số lớn hơn 0!"
            )
            return

        csdl_chi_tieu.them_giao_dich(
            ten, so_tien, loai, danh_muc, ngay, ghi_chu
        )

        messagebox.showinfo("Thông báo", "Thêm giao dịch thành công!")
        self.lam_moi()

    # ==================================
    # HÀM CHỌN GIAO DỊCH
    # ==================================
    def chon_giao_dich(self, event):
        dong_duoc_chon = self.bang.selection()

        if not dong_duoc_chon:
            return

        gia_tri = self.bang.item(dong_duoc_chon[0], "values")

        self.id_dang_chon = gia_tri[0]

        self.o_ten.delete(0, tk.END)
        self.o_ten.insert(0, gia_tri[1])

        self.o_so_tien.delete(0, tk.END)
        self.o_so_tien.insert(0, gia_tri[2])

        self.o_loai.set(gia_tri[3])
        self.o_danh_muc.set(gia_tri[4])

        self.o_ngay.delete(0, tk.END)
        self.o_ngay.insert(0, gia_tri[5])

        self.o_ghi_chu.delete(0, tk.END)
        self.o_ghi_chu.insert(0, gia_tri[6])

    # ==================================
    # HÀM SỬA GIAO DỊCH
    # ==================================
    def sua(self):
        if self.id_dang_chon is None:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn giao dịch cần sửa!"
            )
            return

        ten = self.o_ten.get().strip()
        so_tien = self.o_so_tien.get().strip()
        loai = self.o_loai.get()
        danh_muc = self.o_danh_muc.get()
        ngay = self.o_ngay.get().strip()
        ghi_chu = self.o_ghi_chu.get().strip()

        if not ten or not so_tien or not loai or not ngay:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập đầy đủ thông tin!"
            )
            return

        try:
            so_tien = float(so_tien)
            if so_tien <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Lỗi",
                "Số tiền phải là một số lớn hơn 0!"
            )
            return

        csdl_chi_tieu.sua_giao_dich(
            self.id_dang_chon,
            ten,
            so_tien,
            loai,
            danh_muc,
            ngay,
            ghi_chu
        )

        messagebox.showinfo("Thông báo", "Sửa giao dịch thành công!")
        self.lam_moi()

    # ==================================
    # HÀM XÓA GIAO DỊCH
    # ==================================
    def xoa(self):
        if self.id_dang_chon is None:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn giao dịch cần xóa!"
            )
            return

        xac_nhan = messagebox.askyesno(
            "Xác nhận",
            "Bạn có chắc muốn xóa giao dịch này không?"
        )

        if xac_nhan:
            csdl_chi_tieu.xoa_giao_dich(self.id_dang_chon)
            messagebox.showinfo("Thông báo", "Xóa giao dịch thành công!")
            self.lam_moi()

    # ==================================
    # HÀM LÀM MỚI
    # ==================================
    def lam_moi(self):
        self.id_dang_chon = None

        self.o_ten.delete(0, tk.END)
        self.o_so_tien.delete(0, tk.END)
        self.o_loai.set("")
        self.o_danh_muc.set("")
        self.o_ngay.delete(0, tk.END)
        self.o_ghi_chu.delete(0, tk.END)

        self.bang.selection_remove(self.bang.selection())

        self.hien_thi_giao_dich()

    # ==================================
    # HÀM TÌM KIẾM
    # ==================================
    def tim_kiem(self):
        tu_khoa = self.o_tim_kiem.get().strip()

        danh_sach = csdl_chi_tieu.tim_kiem_giao_dich(tu_khoa)

        for dong in self.bang.get_children():
            self.bang.delete(dong)

        for giao_dich in danh_sach:
            self.bang.insert("", "end", values=giao_dich)


if __name__ == "__main__":
    app = UngDungChiTieu()
    app.mainloop()

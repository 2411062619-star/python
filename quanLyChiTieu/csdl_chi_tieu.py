
import sqlite3


# ==================================
# KẾT NỐI CƠ SỞ DỮ LIỆU
# ==================================
def ket_noi():
    conn = sqlite3.connect("chi_tieu.db")
    return conn


# ==================================
# TẠO BẢNG GIAO DỊCH
# ==================================
def tao_bang():
    conn = ket_noi()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS giao_dich (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten TEXT NOT NULL,
            so_tien REAL NOT NULL,
            loai TEXT NOT NULL,
            danh_muc TEXT,
            ngay TEXT NOT NULL,
            ghi_chu TEXT
        )
    """)

    conn.commit()
    conn.close()


# ==================================
# THÊM GIAO DỊCH
# ==================================
def them_giao_dich(ten, so_tien, loai, danh_muc, ngay, ghi_chu):
    conn = ket_noi()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO giao_dich
        (ten, so_tien, loai, danh_muc, ngay, ghi_chu)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (ten, so_tien, loai, danh_muc, ngay, ghi_chu))

    conn.commit()
    conn.close()


# ==================================
# LẤY DANH SÁCH GIAO DỊCH
# ==================================
def lay_giao_dich():
    conn = ket_noi()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM giao_dich ORDER BY id DESC")

    danh_sach = cursor.fetchall()

    conn.close()

    return danh_sach


# ==================================
# SỬA GIAO DỊCH
# ==================================
def sua_giao_dich(id, ten, so_tien, loai, danh_muc, ngay, ghi_chu):
    conn = ket_noi()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE giao_dich
        SET ten = ?,
            so_tien = ?,
            loai = ?,
            danh_muc = ?,
            ngay = ?,
            ghi_chu = ?
        WHERE id = ?
    """, (ten, so_tien, loai, danh_muc, ngay, ghi_chu, id))

    conn.commit()
    conn.close()


# ==================================
# XÓA GIAO DỊCH
# ==================================
def xoa_giao_dich(id):
    conn = ket_noi()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM giao_dich WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()


# ==================================
# TÌM KIẾM GIAO DỊCH
# ==================================
def tim_kiem_giao_dich(tu_khoa):
    conn = ket_noi()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM giao_dich
        WHERE ten LIKE ?
        ORDER BY id DESC
    """, ("%" + tu_khoa + "%",))

    danh_sach = cursor.fetchall()

    conn.close()

    return danh_sach


# ==================================
# CHẠY TẠO BẢNG KHI MỞ FILE
# ==================================
if __name__ == "__main__":
    tao_bang()
    print("Đã tạo cơ sở dữ liệu và bảng giao dịch thành công!")

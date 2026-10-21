import tkinter as tk
from tkinter import messagebox

def click_button(text):
    current = entry_var.get()
    
    if text == "=":
        try:
            # Hàm eval() giúp tính toán trực tiếp chuỗi biểu thức toán học
            # Thay thế ký hiệu nếu cần, ở đây dùng chuẩn Python (*, /, +, -)
            result = str(eval(current))
            entry_var.set(result)
        except ZeroDivisionError:
            messagebox.showerror("Lỗi", "Không thể chia cho số 0!")
            entry_var.set("")
        except Exception:
            messagebox.showerror("Lỗi", "Biểu thức không hợp lệ!")
            entry_var.set("")
            
    elif text == "C":
        # Xóa toàn bộ màn hình
        entry_var.set("")
        
    else:
        # Nối thêm ký tự vừa bấm vào biểu thức hiện tại
        entry_var.set(current + text)

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Máy Tính Bỏ Túi - Sinh Viên Thực Hiện")
root.geometry("320x450")
root.resizable(False, False)

# Biến lưu trữ giá trị trên màn hình Entry
entry_var = tk.StringVar()

# Tạo ô hiển thị (Entry)
entry_screen = tk.Entry(
    root, 
    textvariable=entry_var, 
    font=("Arial", 22), 
    justify="right", 
    bd=8, 
    relief=tk.GROOVE, 
    bg="#f0f0f0"
)
entry_screen.pack(fill=tk.BOTH, padx=10, pady=15, ipady=10)

# Khung chứa các nút bấm (Button Frame)
btns_frame = tk.Frame(root)
btns_frame.pack(padx=10, pady=5)

# Danh sách các nút bấm và vị trí (Row, Column)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Tạo và bố trí các Button bằng vòng lặp
for (text, row, col) in buttons:
    # Đổi màu sắc cho nổi bật các nút phép toán hoặc nút =
    bg_color = "#e0e0e0"
    if text in ("=", "+", "-", "*", "/"):
        bg_color = "#ffcc00" if text == "=" else "#d0d0d0"
        
    btn = tk.Button(
        btns_frame, 
        text=text, 
        font=("Arial", 16, "bold"), 
        width=5, 
        height=2, 
        bg=bg_color,
        command=lambda t=text: click_button(t)
    )
    btn.grid(row=row, column=col, padx=5, pady=5)

# Chạy vòng lặp ứng dụng
root.mainloop()
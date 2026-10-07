# Quản lý sinh viên bằng Python (CRUD + thống kê)

students = []

def add_student():
    try:
        student_id = input("Nhập mã sinh viên: ")
        name = input("Nhập tên sinh viên: ")
        age = int(input("Nhập tuổi: "))
        major = input("Nhập ngành học: ")
        student = {"id": student_id, "name": name, "age": age, "major": major}
        students.append(student)
        print(" Đã thêm sinh viên thành công!")
    except ValueError:
        print(" Lỗi: tuổi phải là số nguyên.")

def show_students():
    if not students:
        print(" Danh sách sinh viên trống.")
    else:
        print(" Danh sách sinh viên:")
        for s in students:
            print(f"ID: {s['id']} | Tên: {s['name']} | Tuổi: {s['age']} | Ngành: {s['major']}")

def search_student():
    key = input("Nhập mã sinh viên hoặc tên: ")
    found = [s for s in students if s["id"] == key or s["name"] == key]
    if found:
        for s in found:
            print(f" Tìm thấy: {s}")
    else:
        print(" Không tìm thấy sinh viên.")

def delete_student():
    key = input("Nhập mã sinh viên cần xóa: ")
    for s in students:
        if s["id"] == key:
            students.remove(s)
            print(" Đã xóa sinh viên.")
            return
    print(" Không tìm thấy sinh viên để xóa.")

def update_student():
    key = input("Nhập mã sinh viên cần sửa: ")
    for s in students:
        if s["id"] == key:
            try:
                s["name"] = input("Tên mới: ")
                s["age"] = int(input("Tuổi mới: "))
                s["major"] = input("Ngành học mới: ")
                print(" Đã cập nhật thông tin sinh viên.")
            except ValueError:
                print(" Lỗi: tuổi phải là số nguyên.")
            return
    print(" Không tìm thấy sinh viên để sửa.")

def statistics():
    print(f" Tổng số sinh viên: {len(students)}")

def menu():
    while True:
        print("\n--- MENU QUẢN LÝ SINH VIÊN ---")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách")
        print("3. Tìm kiếm sinh viên")
        print("4. Xóa sinh viên")
        print("5. Sửa thông tin sinh viên")
        print("6. Thống kê")
        print("0. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            statistics()
        elif choice == "0":
            print(" Thoát chương trình.")
            break
        else:
            print(" Lựa chọn không hợp lệ.")

# Chạy chương trình
menu()

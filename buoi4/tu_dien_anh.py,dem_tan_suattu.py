#bai6
doan_van = "python la ngon ngu lap trinh python de hoc python de dung"
danh_sach_tu = doan_van.split()
tan_suat = {}
for tu in danh_sach_tu:
  tan_suat[tu] = tan_suat.get(tu, 0) + 1
print("Tan suat xuat hien cac tu:")
for tu, so_lan in tan_suat.items():
  print(f"{tu}: {so_lan}")
  """
  Yêu cầu: Giải thích cách hoạt động của tan_suat.get(tu, 0) + 1 - vì sao chỉ một dòng này đã
thay thế được việc phải kiểm tra "từ đã xuất hiện hay chưa".

tra loi: tan_suat.get(tu, 0) + 1 sẽ lấy giá trị hiện tại của từ tu trong từ điển tan_suat. Nếu từ tu chưa xuất hiện trong từ điển, get() sẽ trả về giá trị mặc định là 0. Sau đó, chúng ta cộng thêm 1 vào giá trị này để tăng số lần xuất hiện của từ tu. Cách này giúp chúng ta không cần phải kiểm tra xem từ tu đã xuất hiện hay chưa, vì nếu chưa xuất hiện, get() sẽ trả về 0 và chúng ta vẫn có thể tăng số lần xuất hiện lên 1.
"""
  

  #bai7
  quan_ly_diem = {
"Nguyen Van A": [8.0, 7.5, 9.0],
"Tran Thi B": [6.0, 6.5, 5.5],
"Le Van C": [9.0, 9.5, 8.5],

}
# Them sinh vien moi
quan_ly_diem["Pham Thi D"] = [7.0, 8.0, 7.5]
# Sua diem mon dau tien cua mot sinh vien
quan_ly_diem["Tran Thi B"][0] = 7.0
diem_trung_binh = {}
for ho_ten, danh_sach_diem in quan_ly_diem.items():
  diem_trung_binh[ho_ten] = round(sum(danh_sach_diem) / len(danh_sach_diem), 2)
print("BANG DIEM TRUNG BINH:")
for ho_ten, dtb in diem_trung_binh.items():
   dat_loai_gioi = dtb >= 8.0
print(f"{ho_ten:<15} - DTB: {dtb:<5} - Dat loai Gioi? {dat_loai_gioi}")
  
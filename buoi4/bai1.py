sinh_vien = {
"ho_ten": "Nguyen Van A",
"nam_sinh": 2004,
"diem_tb": 8.5
}
print(sinh_vien["ho_ten"]) # truy xuat theo khoa
print(sinh_vien.get("diem_tb")) # truy xuat an toan bang get()
print(sinh_vien.get("lop", "Chua co")) # get() voi gia tri mac dinh neu khong co khoa
"""
dung sinh_vien.get("lop", "Chua co") de truy xuat khoa "lop" trong tu dien sinh_vien. Neu khoa "lop" khong ton tai, no se tra ve gia tri mac dinh "Chua co".
"""
#bai1.2
sinh_vien["lop"] = "CNTT01" # them khoa moi
sinh_vien["ten"] = "Binh" # them khoa moi
sinh_vien["diem_tb"] = 8.0 # sua gia tri khoa da co
print(sinh_vien)
diem_cu = sinh_vien.pop("diem_tb") # xoa theo khoa, tra ve gia tri vua xoa

print(sinh_vien, "- diem da xoa:", diem_cu)
sinh_vien.update({"nam_sinh": 2003, "email": "a@example.com"}) # cap nhat/them nhieu

print(sinh_vien)
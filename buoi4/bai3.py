diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}
diem_cong_diem = {mon: round(diem + 0.5, 2) for mon, diem in diem_mon_hoc.items()}
print(diem_cong_diem)
ten_mon_viet_hoa = {mon.upper(): diem for mon, diem in diem_mon_hoc.items()}
print(ten_mon_viet_hoa)

#bai3.2

diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}
diem_cong_diem = {mon: round(diem + 0.5, 2) for mon, diem in diem_mon_hoc.items()}
print(diem_cong_diem)
ten_mon_viet_hoa = {mon.upper(): diem for mon, diem in diem_mon_hoc.items()}
print(ten_mon_viet_hoa)
print(mon_hoc_ky1 - mon_hoc_ky2) # mon chi co o hoc ky 1
"""
tra loi: So sánh Set với Dictionary - Set có lưu cặp khóa-giá trị không? Vì sao Set không cho
phép phần tử trùng lặp la: set chỉ lưu trữ các phần tử duy nhất, không có cặp khóa-giá trị như Dictionary. Do đó, khi so sánh Set với Dictionary, Set sẽ chỉ chứa các phần tử duy nhất từ Dictionary mà không quan tâm đến giá trị của chúng.


"""
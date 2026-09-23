#HOAT DONG 3: Vòng lặp for – range() & duyệt


for i in range(1, 6):
 print(i)

diem_so = [8.5, 7.0, 9.2, 6.5]
for diem in diem_so:
 print("Diem:", diem)
toa_do = (3, 5)
for gia_tri in toa_do:
 print(gia_tri)
diem_mon = {"Toan": 8.0, "Ly": 7.5}
for mon, diem in diem_mon.items():
 print(mon, "-", diem)
ten = "Python"
for ky_tu in ten:
 print(ky_tu)

#Hoạt động 4: Vòng lặp while
#Bài tập 4.1 – Tính giai thừa của n:
n = 5
giai_thua = 1
i = 1
while i <= n:
 giai_thua = giai_thua * i
 i += 1
 print(f"{n}! = {giai_thua}")

#Bài tập 4.2 – Tính tổng các chữ số của một số:
so = 4527
so_tam = so
tong_chu_so = 0
while so_tam > 0:
 chu_so = so_tam % 10
 tong_chu_so += chu_so
 so_tam = so_tam // 10
print(f"Tong cac chu so cua {so} la: {tong_chu_so}")
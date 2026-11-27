import re

chuoi = input("Nhập chuỗi: ")
# Tìm tất cả các số (kể cả số có dấu '-' phía trước)
cac_so = re.findall(r'-?\d+', chuoi)

# Theo ví dụ của đề: "Giá trị dương" = tổng giá trị tuyệt đối của mọi số tìm được,
# "Giá trị âm" = tổng các số có dấu '-' phía trước
tong_duong = sum(abs(int(s)) for s in cac_so)
tong_am = sum(int(s) for s in cac_so if s.startswith('-'))

print(f"Giá trị dương: {tong_duong}. Giá trị âm: {tong_am}.")

import math

x1 = float(input("Nhap hoanh do diem A: "))
y1 = float(input("Nhap tung do diem A: "))
x2 = float(input("Nhap hoanh do diem B: "))
y2 = float(input("Nhap tung do diem B: "))

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Khoang cach giua A({x1}, {y1}) va B({x2}, {y2}) la: {d:.2f}")

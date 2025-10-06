import math

x = float(input('Nhap hoanh do x: '))
y = float(input('Nhap hoanh do y: '))
r = float(input('Nhap ban kinh r: '))

s = math.pi * (r**2)
p = math.pi * 2 * r

print(f"Chu vi duong tron: {p}")
print(f"Dien tich duong tron: {s}")
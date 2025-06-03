# Nhập dữ liệu cho biến name từ bàn phím

def dien_tich_tam_giac(a, h):
    s = (a * h)/2
    print("The area of triangle is", s)

x = int(input("Canh day tam giac la "))
y = int(input("Chieu cao tam giac la "))
dien_tich_tam_giac(x, y)
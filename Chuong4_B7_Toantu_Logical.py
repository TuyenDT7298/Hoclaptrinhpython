def Logical(x, y, z, t):
    print("Result evaluation is", (x > y) or (z < t))

# Nhập dữ liệu cho biến x, y, z, t từ bàn phím
x = int(input("Gia trị cua x là "))
y = int(input("Gia tri cua y la "))
z = int(input("Gia trị cua z là "))
t = int(input("Gia tri cua t la "))
Logical(x, y, z, t)
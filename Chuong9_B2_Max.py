# def Max_3number(a, b, c):
#     Max_number = 0
#     if a > b and a > c:
#         Max_number = a
#     elif b > c:
#         Max_number = b
#     else:
#         Max_number = c
#     print("Gia tri lon nhat trong ba so la", Max_number)
# x = int(input("Nhập số a: "))
# y = int(input("Nhập số b: "))
# z = int(input("Nhập số c: "))
# Max_3number(x, y, z)

def max3(a, b, c):
    if a > b and a > c:
        return a
    return b if b > c else c


a = int(input())
b = int(input())
c = int(input())
print(max3(a, b, c))
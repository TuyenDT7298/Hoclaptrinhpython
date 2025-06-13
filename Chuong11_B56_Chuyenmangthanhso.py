def chuyenmangthanhso(lst):
    so_tu_nhien = int("".join(str(int(x)) for x in lst))
    print("Số tự nhiên tạo thành:", so_tu_nhien)
    
n = int(input("Nhập số lượng phần tử: "))
lst = []

for i in range(n):
    lst.append(int(input("Nhập số ")))
chuyenmangthanhso(lst)
n = int(input("Nhập số lượng phần tử: "))
lst = []
total = 0

for i in range(n):
    lst.append(int(input("Nhập số: ")))
# for i in lst:
#     total += i
# print(total)

def sum_list(lst):
    total = sum(lst)
    print("Tổng các phần tử:", total)

# Gọi hàm
sum_list(lst)
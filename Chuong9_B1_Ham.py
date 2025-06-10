def sum_of_list(lst):
    total = 0
    for j in lst:
        total += j
    print(total)

lst = []
n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    lst.append(int(input("Nhập số: ")))
sum_of_list(lst)
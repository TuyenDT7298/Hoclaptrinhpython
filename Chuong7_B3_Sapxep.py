n = int(input("Nhập số lượng phần tử: "))
lst = []

for i in range(n):
    lst.append(int(input("Nhập số: ")))
lst.sort(reverse=True)
print(lst)

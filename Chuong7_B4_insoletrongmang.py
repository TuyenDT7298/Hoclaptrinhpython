n = int(input("Nhập số lượng phần tử: "))
lst = []

for i in range(n):
    lst.append(int(input("Nhập số: ")))
answer = []
for v in lst:
    if v % 2 != 0:
        answer.append(v)

print(answer)
n = int(input("Nhập số lượng phần tử: "))
lst = []

for i in range(n):
    lst.append(int(input("Nhập số: ")))
answer = []
for v in lst:
    if v % 5 == 0 and v != 0:
        answer.append(v)
if len(answer) == 0:
    answer = [0]
print(answer)
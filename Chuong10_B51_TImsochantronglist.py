def sochan(lst):
    answer = []
    for j in lst:
        if j % 2 == 0:
            answer.append(j)
    print(answer)
n = int(input("Nhập số lượng phần tử: "))
lst = []

for i in range(n):
    lst.append(int(input("Nhập số ")))
sochan(lst)
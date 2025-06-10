def get_unique_values(lst):
    answer = []
    for v in lst:
        if v not in answer:
            answer.append(v)
    return answer   

lst = []
n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    lst.append(int(input("Nhập số: ")))
get_unique_values(lst)
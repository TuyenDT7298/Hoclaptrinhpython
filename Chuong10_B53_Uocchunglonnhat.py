def power(a, b):
    lst = []
    # if a >= b:
    for c in range(1, max(a, b)):
        if a % c == 0 and b % c == 0:
            lst.append(c)
    print(max(lst))
    # else:
    #     for c in range(1, b + 1):
    #         if a % c == 0 and b % c == 0:
    #             lst.append(c)
    #     print(max(lst))

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
power(a, b)
def Toantu(a, total):
    total += a # Using += Operator
    print("The Value of the Total after using += Operator is:", total)
    total -= a # Using -= Operator
    print("The Value of the Total after using -= Operator is:", total)
    total *= a # Using *= Operator
    print("The Value of the Total after using *= Operator is:", total)
    total //= a # Using //= Operator
    print("The Value of the Total after using //= Operator is:", total)
    total **= a # Using **= Operator
    print("The Value of the Total after using **= Operator is:", total)
    total /= a # Using /= Operator
    print("The Value of the Total after using /= Operator is:", total)
    total %= a # Using %= Operator
    print("The Value of the Total after using %= Operator is:", total)

# Nhập dữ liệu cho biến a, total từ bàn phím
a = float(input("Gia trị cua a là "))
total = float(input("Gia tri cua total la "))
Toantu(a, total)




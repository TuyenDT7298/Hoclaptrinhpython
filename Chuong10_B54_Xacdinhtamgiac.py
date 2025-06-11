def tamgiac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Equilateral triangle")
        elif a == b or a == c or b == c:
            print("Isosceles triangle")
        else:
            print("Scalene triangle")
    else:
        print("Không phải là tam giác")
    
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
tamgiac(a, b, c)
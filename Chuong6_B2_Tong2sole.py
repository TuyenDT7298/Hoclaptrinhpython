a = int(input("Input a = "))
b = int(input("Input b = "))
answer = 0
while a <= b:
    if a % 2 != 0:
        answer += a
    a += 1
print("Tổng các số lẻ từ a đến b là:", answer)
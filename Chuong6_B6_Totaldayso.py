a = int(input("Nhập số a = "))
Total = 0

for i in range (0, a):
    Total += (i+1)/(i+2)

print("Total =", round(Total, 2))
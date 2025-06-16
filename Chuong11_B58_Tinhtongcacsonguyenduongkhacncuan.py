def sumOfAll(n):
    Answer = 0
    for i in range(1, n):  
        if n % i == 0:
            Answer += i 
    print(Answer)

n = int(input())
sumOfAll(n)
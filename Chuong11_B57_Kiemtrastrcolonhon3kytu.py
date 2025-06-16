def timkutulonhon3(n):  
    if len(n) > 3:
        if n[-3:] == "ing":
            print(str(n) + "ly")
        else:
            print(str(n) + "ing")    
    else:
        print(n)
    
n = str(input())
timkutulonhon3(n)
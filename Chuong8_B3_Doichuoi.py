def string1(text1, text2):
    tmp = text1[0:2] + text2[2:]
    text1 = text2[0:2] + text1[2:]
    text2 = tmp
    print(text1 + " " + text2)
x = input("Chuoi ky tu ban dau la ")
y = input("Chuoi ky tu ban dau la ")
string1(x, y)
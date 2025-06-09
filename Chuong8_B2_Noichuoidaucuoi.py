def string1(text):
    if len(text) < 2:
        print("")
    else:
        print("Chuoi 2 ky tu dau + 2 ky tu cuoi la", text[0:2] + text[-2:])

x = input("Chuoi ky tu ban dau la ")
string1(x)
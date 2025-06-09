def string1(text):
    words = text.split()           # Tách chuỗi thành danh sách các từ
    reversed_words = words[::-1]  # Đảo ngược danh sách từ
    result = " ".join(reversed_words)  # Ghép lại thành chuỗi
    print("Chuỗi sau khi đảo ngược các từ:", result)

x = input("Chuoi ky tu ban dau la ")
string1(x)
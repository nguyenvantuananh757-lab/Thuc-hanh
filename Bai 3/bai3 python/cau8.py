print("sinh vien : nguyen van tuan anh")

print("ma so sv :245751030110037")

print("#############################")
#cau 8
words = input("Nhập các từ: ").split()

max_len = max(len(w) for w in words)

print("Các từ dài nhất:")
for w in words:
    if len(w) == max_len:
        print(w)


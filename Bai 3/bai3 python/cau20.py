print("sinh vien : nguyen van tuan anh")

print("ma so sv :245751030110037")

print("#############################")
#cau 20
n = int(input("Nhập n: "))

# mỗi dòng là một list
triangle = []

for i in range(n):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)

# in tam giác Pascal
for row in triangle:
    print(row)


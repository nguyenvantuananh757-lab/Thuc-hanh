print("sinh vien : nguyen van tuan anh")

print("ma so sv :245751030110037")

print("#############################")
#cau 1
class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

# Ví dụ sử dụng
aCircle = Circle(2)
print(aCircle.area())


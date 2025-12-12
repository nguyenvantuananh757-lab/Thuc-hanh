print("sinh vien : nguyen van tuan anh")

print("ma so sv :245751030110037")

print("#############################")
#cau 3
class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Ví dụ sử dụng
aNam = Nam()
aNu = Nu()

print(aNam.getGender())
print(aNu.getGender())


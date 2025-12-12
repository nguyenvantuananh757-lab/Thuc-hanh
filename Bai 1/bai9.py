print("sinh vien : nguyen van tuan anh")

print("ma so sv :245751030110037")

print("#############################")
str = input("enter a string:")
dict={}
for n in str:
    keys=dict.keys()
    if n in keys:
        dict[n]+=1
    else:
        dict[n]=1
        print(dict)


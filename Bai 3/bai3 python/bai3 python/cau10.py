#cau 10
ds=input('Nhap chuoi: ').split()
if len(ds) >= 2:
    new_ds = ds[1:-1]
else:
    new_ds = []

print("List sau khi bỏ phần tử đầu và cuối:", new_ds)

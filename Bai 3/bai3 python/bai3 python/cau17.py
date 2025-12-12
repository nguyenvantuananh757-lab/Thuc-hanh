#cau 17
n = int(input("Nhập n: "))

def sum_divisors(x):
    s = 0
    for i in range(1, x):
        if x % i == 0:
            s += i
    return s

for x in range(1, n):
    if sum_divisors(x) > x:
        print(x)

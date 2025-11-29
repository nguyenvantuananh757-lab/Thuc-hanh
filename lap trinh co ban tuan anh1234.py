print("NGUYEN VAN TUAN ANH")
print("msv 245751030110037")
print("1)")
n1=int(input("nhap n1 tu ban phim"))
n2=int(input("nhap n2 tu ban phim"))
if n1>n2:
    print("n1 lon hon n2")
elif n2>n1:    
    print("n2 lon hon n1")
elif n1==n2:
    print("n1 bang n2")
print("2)")
import math;
x1=int(input("nhap tu ban phim x1--->"))
y1=int(input("nhap tu ban phim y1--->"))
x2=int(input("nhap tu ban phim x2--->"))
y2=int(input("nhap tu ban phim y2--->"))
d1=(x2-x1)*(x2-x1); 
d2=(y2-y1)*(y2-y1);
res=math.sqrt(d1+d2)
print("khoang cach giua hai diem:",res);
print("3)")
n=int(input("nhap 1 so bat ki----->"))
if n%2==0:
    print("so chan");
else:
    print("so le");
print("4)")
a=int(input("nhap a tu ban phim"))
b=int(input("nhap b tu ban phim"))
i=1;
for j in range(a,b):
    print("i:",i,"j:",j)
    print(i,"/",j)
    print(i/j);
print("5)")    
n=int(input("nhap 1 so bat ki---."));
while n>=0:
        print (n);
        n= n-1;
print("6)")
j=[]
for i in range (2000,3201):
    if (i%7==0)and(i%5!=0):
        j.append(str(i))
print(','.join(j))
print("7)")
n=int(input("nhap vao mot so:"))
d=dict()
for i in range (1,n+1):
    d[i]=i*i
print(d)
print("8)")
a,b=1,2
total=0
print(a,end=" ")
while(a<=4000000-1):
    print(a,end=" ")
    if a%2==0:
        total +=a
    a,b=b,a+b
print("\n tong cac so chan trong day Fibonnaci:",total)
print("9)")
str=input("nhap xau ki tu:")
dict={}
for i in str:
    dict[i]=str.count(i)
print(dict)
print("10)")
a=input("nhap xau ky tu:")
print(a)
b=a.split()
print (b)
c=" ".join(b)
print(c)
print("11)")
l=[1,"python",4,7]
k=['cse',2,'guntur',8]
m=[]
m.append(l);
m.append(k);
print(m)
d={1:l,2:k,'combine_list':m}
print(d)
print("12)")
        


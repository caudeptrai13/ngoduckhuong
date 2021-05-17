import math
a, b, c =map(int, input("Nhap a, b, c: ").split())

p = (a + b + c)/2
p = p*(p-a)*(p-b)*(p-c)
if p > 0:
    print("Chu vi :", a + b + c)
    print("Dien tich: ", math.sqrt(p))
else:
    print("Khong phai hinh tam giac")
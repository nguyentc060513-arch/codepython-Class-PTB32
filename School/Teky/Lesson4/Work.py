#BÀI TẬP NHẬP LIỆU VÀ TOÁN TỬ CƠ BẢN
#1
n = float(input("Nhập 1 số bất kì: "))
print(n * 3 + 1)
#2
n = float(input("Nhập 1 số bất kì: "))
print((n ** 2)/3)
#3
c = float(input("Hãy nhập nhiệt độ c"))
print("Nhiệt độ f là: ", c * 1.8 + 32)
#4
a = int(input("Nhập số nguyên a bất kì: "))
if a % 2 == 0 :
    print(True)
else :
    print(False)
#5
a = int(input("Nhập số nguyên a bất kì: "))
if a >= 50 and a <= 100 :
    if a % 3 :
        print(True)
    else :
        print(False)
else :
    print("Không hợp lệ")
#6
a = int(input("Nhập số nguyên a bất kì: "))
if a % 5 :
    if not a >= 20 and a <= 50 :
        print(True)
    else :
        print(False)
else :
    print("Thông số không hợp lệ")        
#7
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
if a % 2 == 0 or b % 2 == 0:
    print(True)
else :
    print(False)
#8
a_str = input("Nhập một số thực: ")
try:
    a = float(a_str)
    if a.is_integer():
        print(True)
    else:
        print(False)
except ValueError:
    print("Vui lòng nhập một số thực hợp lệ.")
#9
import math
a = int(input("Nhập số nguyên a: "))
def la_so_chinh_phuong(a):
  if a < 0:
    return False
  can_a = math.sqrt(a)
  return int(can_a) * int(can_a) == a
print(la_so_chinh_phuong(a))
print(la_so_chinh_phuong(a))
print(la_so_chinh_phuong(a))
#10
tien_luong = float(input("Nhập số tiền"))
if tien_luong < 0 :
    print("Vợ bạn sẽ nổi giận")
else :
    print("Vì đưa cho vợ 90%,số tiền bạn còn lại là: " , tien_luong * 0.1)
#11
a = float(input("Nhập số bất kì: "))
b = float(input("Nhập số bất kì: "))
c = float(input("Nhập số bất kì: "))
print("tổng của 3 số là: ", a + b + c)
#12
a = float(input("Nhập số bất kì: "))
b = float(input("Nhập số bất kì: "))
c = float(input("Nhập số bất kì: "))
d = (a + b)^c
print("d là: ", d)
if d >= 100 and d <= 200 :
    print(True)
else:
    print(False)
#BÀI TẬP LỆNH ĐIỀU KIỆN CƠ BẢN
#1
a = int(input("Nhập số nguyên a: "))
if a < 0 :
    print("a phải là số nguyên dương")
else :
    if a > 10 :
        print("đây là số lớn hơn 10")
    else :
        print("đây là số bé hơn 10")
#2
a = int(input("Nhập số nguyên a: "))
if a % 2 == 0 :
    print("Số chẵn")
else :
    print("Số lẻ")
#3
a = float(input("Nhập số bất kì: "))
b = float(input("Nhập số bất kì: "))
c = float(input("Nhập số bất kì: "))
if a > 0 and b > 0 and c > 0 :
    if a + b > c and b + c > a and c + a > b :
        print("Thỏa mãn")
    else : 
        print("Không thỏa mãn")
else :
    print("Cả ba số phải lớn hơn 0")
#4
a = float(input("Nhập số bất kì: "))
b = float(input("Nhập số bất kì: "))
c = float(input("Nhập số bất kì: "))

if a > 0 and b > 0 and c > 0 :
    if a + b > c and b + c > a and c + a > b :
        if a == b == c :
            print("Đây là tam giác đều")
        elif (a^2 == b^2 + c^2 and c == b) or (b^2 == a^2 + c^2 and a == c) or (c^2 == b^2 + a^2 and b == a) :
            print("Đây là tam giác vuông cân")
        elif (a^2 == b^2 + c^2) or (b^2 == a^2 + c^2) or (c^2 == b^2 + a^2)  :
            print("Đây là tam giác vuông")
        elif  a == b or b == c or c == a :
            print("Tam giác cân")
        else : 
            print("Tam giác thường")
    
else :
    print("Ko phải tam giác")
#5
a = float(input("Nhập số bất kì: "))
b = float(input("Nhập số bất kì: "))
c = float(input("Nhập số bất kì: "))
list = [a,b,c]
list.sort
print(list)
#6
print("Phương trình ax + b = 0")
a = float(input("Nhập biến a: "))
b = float(input("Nhập số b"))
if a == 0 and b != 0 :
    print("Vô nghiệm")
elif a == 0 and b == 0:
    print("Vô số nghiệm")
else :
    print("Nghiệm là: ", -b/a)
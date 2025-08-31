"""1,b/2,a/3,a/4,b/5,b/6,c/7,a/8,a/9,a/10,c"""
import math

ds_nguyen_to = []
tong = 0

for so in range(2, 100):
    la_nguyen_to = True
    for i in range(2, int(math.sqrt(so)) + 1):
        if so % i == 0:
            la_nguyen_to = False
            break
    if la_nguyen_to:
        ds_nguyen_to.append(so)
        tong += so

print("Cac so nguyen to be hon 100:")
print(ds_nguyen_to)
print("Tong cac so nguyen to tren la:", tong)





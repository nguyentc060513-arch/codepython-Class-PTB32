'''
1.D
2.A
3.A
4.B
5.B
6.C
7.C
8.A
9.A
10.C
'''
tong = 0
print("Các số nguyên tố bé hơn 100:")

for so in range(2, 100):
    if all(so % i != 0 for i in range(2, so)):
        print(so, end=" ")
        tong += so

print("\nTổng =", tong)
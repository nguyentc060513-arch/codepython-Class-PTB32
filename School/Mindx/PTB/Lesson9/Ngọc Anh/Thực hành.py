def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

tong = 0
print("Các số nguyên tố bé hơn 100 là:")
for so in range(2, 100):
    if la_so_nguyen_to(so):
        print(so, end=" ")
        tong += so

print("\nTổng các số nguyên tố trên:", tong)
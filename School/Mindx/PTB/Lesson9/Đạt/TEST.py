tong = 0
print("Các số nguyên tố bé hơn 100 là:")

i = 2
while i < 100:      
    la_nguyen_to = True
    j = 2
    while j < i:
        if i % j == 0:
            la_nguyen_to = False
            break
        j += 1

    if la_nguyen_to:
        print(i, end=" ")
        tong += i

    i += 1

print("\nTổng của các số nguyên tố bé hơn 100 là:", tong)

tong = 0
print("Các số nguyên tố bé hơn 100 là:")

for n in range(2, 100): 
    is_prime = True
    for i in range(2, n):
        if n % i == 0: 
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")
        tong += n 

print("\nTổng các số nguyên tố là:", tong)

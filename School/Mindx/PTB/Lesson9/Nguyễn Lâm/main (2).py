def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_sum = 0

print("Các số nguyên tố bé hơn 99 là:")
for i in range(2, 99):
    if is_prime(i):
        print(i, end=" ")
        prime_sum += i

print("\nTổng các số nguyên tố trên là:", prime_sum)
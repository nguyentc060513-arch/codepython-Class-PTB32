'''
1-B
2-C
3-B
4-C
5-D
6-B
7-C
8-D
9-C
10-C
'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = []
for i in range(2, 100):
    if is_prime(i):
        prime_numbers.append(i)

print("Các số nguyên tố bé hơn 100 là:")
print(prime_numbers)

tong = sum(prime_numbers)
print("Tổng các số nguyên tố đó là:", tong)


 

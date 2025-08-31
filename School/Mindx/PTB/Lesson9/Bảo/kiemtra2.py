
def so_nguyen_to(n): 
    if n < 2:
        return False 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

tong = 0
for num in range(2, 100):
    if so_nguyen_to(num):
        print(num, end=" ")
        tong += num

print("\nTổng các số nguyên tố nhỏ hơn 100 là:", tong)


    
        

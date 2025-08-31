# dem cac so nguyen to be hon 100
def la_so_nguyen_to(n):
    if n < 2:
        return False
    # xác định các số bé hơn 100 mà vẫn chia hết cho 1 và chính nó
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

tong = 0
print("Các số nguyên tố nhỏ hơn 100 là:")
# Tổng so nguyên tố
for i in range(2, 100): # nằng trong khoảng từ 2 đến 100
    if la_so_nguyen_to(i):#dựa từ những số được đếm dưới 100 dể cộng vào nhau
        print(i, end=' ')
        tong += i

print("\nTổng các số nguyên tố nhỏ hơn 100 là:", tong)
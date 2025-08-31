'''
    Hàm: Là một khối mã được đặt tên sử dụng dể thực hiện 1 loạt hành động cụ thể.
Hàm cho phép chia nhỏ chương trình thành các phần nhỏ, giúp quản lý các đoạn mã 
dễ hơn, Hàm có thể tái sử dụng lại nếu chương trình cần 
'''
# Tính tổng 2 số 
def tong_hai_so(a, b): # a và b là tham số 
    tong = a + b
    return tong

# Cách gán giá trị gán gián tiếp
c = 10
d = 20 
ket_qua = tong_hai_so(c, d)
# Cách gán giá trị trự tiếp
ket_qua2 = tong_hai_so(40, 50)

print(f"Tổng của {c} và {d} là: {ket_qua}")
print(f"Tổng của a và b là: {ket_qua2}")

# Hàm không tham số 
def in_ket_qua():
    print("Kết quả là")

in_ket_qua()
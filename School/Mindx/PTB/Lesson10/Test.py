# # Nhập số lượng bài tập
# n = int(input("Nhập số nguyên dương n: "))
# if n <= 0:
#     print("Vui lòng nhập số nguyên dương!")
# else:
#     diem_bai_tap = []
#     for i in range(n):
#         diem = float(input(f"Nhập điểm cho bài tập {i+1}: "))
#         diem_bai_tap.append(diem)
#     print("Danh sách điểm các bài tập:", diem_bai_tap)
# #1
# diem_bai_tap.sort()
# print(f"Điểm bài tập sai khi được sắp xếp là:{diem_bai_tap}")
# # 2
# diem_be_nhat = diem_bai_tap[0]
# so_lan = diem_bai_tap.count(diem_be_nhat)
# for i in range(so_lan) :
#     diem_bai_tap.remove(diem_be_nhat)
# print(f"Điểm bài tập sau khi xóa đi điểm bé nhất là {diem_bai_tap}")
# #4
# count = 0
# for i in range(len(diem_bai_tap)) :
#     if diem_bai_tap[i] >= 8 :
#         count += 1
#     else :
#         count += 0
# print(f"Số bài tập điểm lớn hơn 8 là: {count}")
#
# n = int(input("Nhập số n: "))
# tong = 0
# i = 0
# # for i in range(n + 1) :
# #     tong += i
# # print(tong)
# while True :
#     if i < n :
#         i += 1
#         tong += i
#     else :
#         break
# print(tong)

#
    # products = [
#     "Pphone_1",
#     "Pphone_2",
#     "Pphone_3",
#     "Pphone_4",
#     "Pphone_5",
#     "Pphone_6",
#     "Pphone_7",
#     "Pphone_8",
#     "Pphone_9",
#     "Pphone_10"
# ]
# giohang = []

# while True:
#     yeucau = int(input("Bạn muốn yêu cầu nào (1:Xem giỏ hàng, 2:Thêm sản phẩm, 3:Xóa sản phẩm, 4:Thoát, 5:Xem sản phẩm): "))

#     if yeucau == 1:
#         if not giohang:
#             print("Giỏ hàng trống!")
#         else:
#             print("--- Giỏ hàng của bạn ---")
#             for i, sp in enumerate(giohang, 1):
#                 print(f"{i}. {sp}")
#     elif yeucau == 2:
#         print("--- Danh sách sản phẩm ---")
#         for i, sp in enumerate(products, 1):
#             print(f"{i}. {sp}")
#         them_san_pham = int(input("Bạn muốn thêm sản phẩm số mấy: "))
#         giohang.append(products[them_san_pham - 1])
#         print(f"Đã thêm {products[them_san_pham - 1]} vào giỏ hàng!")
#     elif yeucau == 3:
#         if not giohang:
#             print("Giỏ hàng trống!")
#             continue
#         print("--- Giỏ hàng ---")
#         for i, sp in enumerate(giohang, 1):
#             print(f"{i}. {sp}")
#         xoa_san_pham = int(input("Bạn muốn xóa sản phẩm số mấy: "))
#         removed = giohang.pop(xoa_san_pham - 1)
#         print(f"Đã xoá {removed} khỏi giỏ hàng!")
#     elif yeucau == 4:
#         print("Thoát chương trình!")
#         break
#     elif yeucau == 5:
#         print("--- Danh sách sản phẩm ---")
#         for i, sp in enumerate(products, 1):
#             print(f"{i}. {sp}")
#     else:
#         print("Lựa chọn không hợp lệ!")
# def hiengiohang() :
#     global giohang
#     print(giohang)
# def thoat_chuong_trinh() :
#     print("Exit")
# def hienmathang() :
#     global products
#     print(products)
# products = [
#     "Pphone_1",
#     "Pphone_2",
#     "Pphone_3",
#     "Pphone_4",
#     "Pphone_5",
#     "Pphone_6",
#     "Pphone_7",
#     "Pphone_8",
#     "Pphone_9",
#     "Pphone_10"
# ]
# giohang = []
# while True :
#     yeucau = int(input("Bạn muốn yêu cầu nào(1:Xem giỏ hàng,2:Thêm sản phẩm vào giỏ hàng,3:Xóa sản phẩm khỏi giỏ hàng,4:Thoát chương trình,5: Xem sản phẩm) : "))
#     if yeucau == 1 :
#         hiengiohang()
#         continue
#     elif yeucau == 2 :
#         them_san_pham = int(input("Bạn muốn thêm sản phẩm nào(ghi số 1,2,3,4,...) : "))
#         giohang.append(products[them_san_pham - 1])
#         continue
#     elif yeucau == 3 :
#         xoa_san_pham = int(input("Bạn muốn xóa sản phẩm số mấy: "))
#         giohang.remove(xoa_san_pham)
#         continue
#     elif yeucau == 4 :
#         thoat_chuong_trinh()
#         break    
#     elif yeucau == 5 :
#         hienmathang()
#         continue
    

# 1.Hien thi san pham
def product_list(product) :
    # Hien thi san pham
    for index in range(len(product)) :
        print(f"{index + 1}: {product[index]}")
# 2.Goi ham product_list de hien thi san pham:
def shopping_list(Shopping_list) :
    # Khi gio hang rong
    if not Shopping_list : # Neu gio hang rong
        print("Chưa có sản phẩm trong giỏ hàng")
    else :
        print("Mặt hàng của bạn bao gồm là: ")
        for index in range(len(Shopping_list)) :
            print(f"{index + 1} : {Shopping_list[index]}")
# 3.Thêm sản phẩm vào giỏ hàng
def add_product(product,Shopping_list) :
    print("Danh sách sản phẩm là: ")
    product_list(product) # Gọi lại hàm product_list(product) để hiện thị sản phẩm
    # Tạo chức năng lấy sản phẩm
    # Tạo biến số lưu trữ vị trí sản phẩm
    item_index = int(input("Hãy chọn sản phẩm bạn muốn thêm vào:")) - 1
    if item_index >= 0 and item_index < len(product) :
        select_item = product[item_index] # Tạo biến số lưu trữ sản phẩm đã chọn\
        Shopping_list.append(select_item)
        print(f"{select_item} đã được thêm vào giỏ hàng của bạn")
    else :
        print("Sản phẩm không hợp lệ")
# 4.Xóa sản phẩm khỏi giỏ hàng
def delete_shopping_list(Shopping_list) :
    if not Shopping_list :
        print("Giỏ hàng của bạn đang trống")
    else :
        print("Các sản phẩm có trong giỏ hàng là: ")
        shopping_list(Shopping_list)
        item_index = int(input("Nhập vị trí sản phẩm bạn muốn xóa: ")) -1
        if item_index >= 0 and item_index < len(Shopping_list) :
            delete_item = Shopping_list.pop(item_index)
            print(f"{delete_item} đã được xóa ra khỏi giỏ hàng")
        else :
            print("Không hợp lệ")
# Hàm quản lý chương trình
def main() :
    product = ["Apple","Samsung","Lenovo","Iphone","Ipad"]
    Shopping_list = []
    while True :
        print("1.Danh sách sản phẩm")
        print("2.Xem giỏ hàng")
        print("3.Thêm sản phẩm vào giỏ hàng")
        print("4.Xóa sản phẩm ra khỏi giỏ hàng")
        print("5.Thoát chương trình")
        choice = int(input("Nhập tính năng bạn muốn lựa chọn(Từ 1-5): "))
        if choice == 1:
            product_list(product)
        elif choice == 2:
            shopping_list(Shopping_list)
        elif choice == 3:
            add_product(product,Shopping_list)
        elif choice == 4:
            delete_shopping_list(Shopping_list)
        elif choice == 5:
            break
        
main()
'''
    Xâu chuỗi trong python có thể hiểu là chuỗi kỹ tự strings
    1. Tạo chuỗi 
    2. Nốt chuỗi
    3. Truy cập vị trị của chuỗi
    4. Cắt chuỗi
    5. Định dạng của chuỗi
    6. Các phương thức của chuỗi
'''
# 1 Tạo chuỗi: Được khai báo trong dấu nháy đơn  (' ') hoặc nháy kép (" ")
name = "Hưng"
age = 90
print("Đây là kiểu dữ liệu của age: ", type(age))

# 2. Nối chuỗi: sử dụng toán tử (+) - chỉ được nối chuỗi bởi kiểu dữ liệu string
address = "Hà Lội"
info = name + " Sống ở: " + address + " tuổi: " + str(age)
print(info)

# 3.Truy cập vị trí của chuỗi: Sử dụng index để truy cập vị trí
# Khoảng trắng cũng được tính là 1 đơn vị index 
name = "Vũ Lâm"
index_name = name[5]
print("Vị trí của 5 là: ", index_name)

# 4. Cắt chuỗi: Sử dụng index để cắt theo vị trí 
strings = "0123456789"
print(strings[3:7]) # Cắt từ vị trí 3 đến 7
print(strings[ :4]) # Cắt từ vị trí từ 0 cho đến 4
print(strings[5: ]) # Cắt từ vị trí 5 cho đến hết 

# 5. Định dạng của chuỗi: Gồm 3 định dạng
name = "Thành Hưng"
address = "Nghệ An"
age = 18

# Định dạng thường 
print("Tên tôi là ", name, " Địa chỉ: ", address, " Tuổi là: ", str(age))
# Định dạng sử dụng "format()"
print("TÊN TÔI LÀ: {} ĐỊA CHỈ: {} TUỔI LÀ: {}".format(name, address, str(age)))
# Định dạng sử dụng f""
print(f"Tên tôi là {name} Địa chỉ là {address} tuổi là: {str(age)}")


# 6.Các phương thức của chuỗi
# Phương thức upper(): Chuyển đổi chuỗi thành chữ hoa
name = "Lâm"
print(f"Sử dụng upper(): {name.upper()}")
# Phương thức lower(): Chuyển đổi chuỗi thành chữ thường
name = "LÂM"
print(f"Sử dụng lower(): {name.lower()}")

# split(): Sử dụng để chuyển đổi chuỗi sang danh sách (list)
strings = "Thầy.Hưng.đẹp.Trai"
strings_list = strings.split(".")
print(f"strings sau khi tách bởi split(): {strings_list}")

# find(), index(): Tìm vị trí xuất hiện- nếu không tìm thấy kết quả sẽ trả ra -1 nếu dùng find()
new_Strings = "Nguyên rất xấu xa"
print(new_Strings.find("xấu"))
print(new_Strings.index("xấu"))

# replace(): Thay thế các trường hợp của một chuỗi khác
# Chú ý: Bắt buộc giá trị thay đổi phải thuộc string
string2 = "Lâm rất xấu trai"
new_Strings2 = string2.replace("xấu", "không đẹp")
print(new_Strings2)
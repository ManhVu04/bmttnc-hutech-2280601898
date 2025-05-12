# Hãy phát triển một chương trình để nhập vào một chuỗi các số nhị phân
# với 4 chữ số, phân cách bằng dấu phẩy. Chương trình sẽ kiểm tra từng số để xác
# định xem chúng có chia hết cho 5 hay không, sau đó in ra những số thỏa mãn điều
# kiện này, cũng được phân tách bằng dấu phẩy. Ví dụ, nếu đầu vào là: ‘0100’,
# ‘0011’, ‘1010’, ‘1001’, thì kết quả đầu ra sẽ là: ‘1010’.

# Nhập vào chuỗi các số nhị phân, phân cách bằng dấu phẩy
input_str = input("Nhập các số nhị phân, phân cách bằng dấu phẩy: ")
binaries = input_str.split(',')

# Lọc ra các số chia hết cho 5
result = []
for b in binaries:
    b = b.strip()  # Loại bỏ khoảng trắng thừa
    if int(b, 2) % 5 == 0:
        result.append(b)

# In kết quả, phân tách bằng dấu phẩy
print("Các số nhị phân chia hết cho 5 là:", ', '.join(result))\
# In kết quả, phân tách bằng dấu phẩy




















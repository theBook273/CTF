# 1. Đọc file chứa chuỗi nhị phân (thay 'digits.bin' bằng tên file của bạn)
with open("digits.bin", "r") as f:
    binary_string = f.read().strip()

# Loại bỏ các khoảng trắng hoặc xuống dòng nếu có
binary_string = binary_string.replace(" ", "").replace("\n", "")

# 2. Chuyển đổi chuỗi 8-bit thành các byte dữ liệu
image_bytes = bytearray()
for i in range(0, len(binary_string), 8):
    byte = binary_string[i : i + 8]
    if len(byte) == 8:  # Đảm bảo đủ 8 bit
        image_bytes.append(int(byte, 2))

# 3. Ghi dữ liệu byte vào file ảnh mới
with open("flag.jpg", "wb") as f:
    f.write(image_bytes)

print("Đã chuyển đổi thành công! Hãy mở file flag.jpg để xem kết quả.")

def bin_to_dec(binary_str):
    # 将二进制字符串转换为十进制整数
    return str(int(binary_str, 2))

def dec_to_bin(decimal_str):
    # 将十进制字符串转换为二进制字符串
    decimal_int = int(decimal_str)
    return bin(decimal_int)[2:]

def hex_to_dec(hex_str):
    # 将十六进制字符串转换为十进制整数
    return str(int(hex_str, 16))

def dec_to_hex(decimal_str):
    # 将十进制字符串转换为十六进制字符串
    decimal_int = int(decimal_str)
    return hex(decimal_int)[2:].upper()

def bin_to_hex(binary_str):
    # 将二进制字符串转换为十六进制字符串
    decimal_str = bin_to_dec(binary_str)
    return dec_to_hex(decimal_str)

def hex_to_bin(hex_str):
    # 将十六进制字符串转换为二进制字符串
    decimal_str = hex_to_dec(hex_str)
    return dec_to_bin(decimal_str)
# 输入二进制，转换为十进制字符串输出
binary_str = "1101"
decimal_str = bin_to_dec(binary_str)
print(f"{binary_str} in binary is {decimal_str} in decimal.")

# 将十进制字符串转换为二进制字符串
decimal_str = "10"
binary_str = dec_to_bin(decimal_str)
print(f"{decimal_str} in decimal is {binary_str} in binary.")

# 将十六进制字符串转换为十进制字符串
hex_str = "64"
decimal_str = hex_to_dec(hex_str)
print(f"{hex_str} in hexadecimal is {decimal_str} in decimal.")

# 将十进制字符串转换为十六进制字符串
decimal_str = "100"
hex_str = dec_to_hex(decimal_str)
print(f"{decimal_str} in decimal is {hex_str} in hexadecimal.")

# 将二进制字符串转换为十六进制字符串
binary_str = "1100100"
hex_str = bin_to_hex(binary_str)
print(f"{binary_str} in binary is {hex_str} in hexadecimal.")

# 将十六进制字符串转换为二进制字符串
hex_str = "64"
binary_str = hex_to_bin(hex_str)
print(f"{hex_str} in hexadecimal is {binary_str} in binary.")

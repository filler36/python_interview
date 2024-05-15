input_str = 'ы'

# Convert string to bytes with utf-8 encoding
input_str_bytes = bytes(input_str, 'utf-8')
print(input_str_bytes)  # b'\xd1\x8b'

# Convert bytes to list of bytes represented as binary
print([bin(byte) for byte in input_str_bytes])  # ['0b11010001', '0b10001011']

# Convert bytes to list of bytes represented as integers
print([byte for byte in input_str_bytes])  # [209, 139]

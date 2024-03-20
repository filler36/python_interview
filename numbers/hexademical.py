a = 0xA0  # 10*16**1 + 0*16**0 = 160
print(a)  # 160
print(int(a))  # 160
print(hex(a))  # 0xa0 hex() returns str not int
print(f'{a:x}')  # a0
print(f'{a:X}')  # A0
print(f'{a:03X}')  # 0A0

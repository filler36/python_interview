a = 0o22  # 2*8**1 + 2*8**0 = 18
print(a)  # 18
print(int(a))  # 18
print(oct(a))  # 0o22 oct() returns str not int
print(f'{a:o}')  # 22
print(f'{a:03o}')  # 022

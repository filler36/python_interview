str1 = 'Hello'
print(str1.startswith('H'))  # True
print(str1.startswith('el', 1, 1))  # False
print(str1.startswith('el', 1, 3))  # True
print(str1.startswith('H'))  # True
print('\n', end='')
print(str1.endswith('o'))  # True
print(str1.endswith('O'))  # False

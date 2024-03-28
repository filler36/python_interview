str1 = 'Hello'
print('\n', end='')
print(str1.find('H'))  # 0
print(str1.find('l'))  # 2
print(str1.find('l', 3))  # 3
print(str1.find('x'))  # -1
print('\n', end='')
print(str1.replace('l', 'h'))  # Hehho
print(str1.replace('l', 'h', 1))  # Hehlo
print('\n', end='')
print(str1.index('H'))  # 0
print(str1.index('l'))  # 2
print(str1.index('x'))  # ValueError: substring not found
''' Both index() and find() are identical in that they return the index position of the first occurrence
of the substring from the main string. The main difference is that Python find() produces -1 as output if it is unable
to find the substring, whereas index() throws a ValueError exception'''

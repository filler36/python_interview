str1 = 'Hello'
str2 = 'Hello world'
str3 = '12345'
str4 = '0x11'

print('--- ISNUMERIC')  # A string is numeric if all characters in the string are numeric and there is at least one character in the string
print(str1.isnumeric())  # False
print(str3.isnumeric())  # True
print(str4.isnumeric())  # False
print('--- ISALPHA')  # A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string
print(str1.isalpha())  # True
print(str2.isalpha())  # False
print(str3.isalpha())  # False
print(str4.isalpha())  # False
print('--- ISASCII')  # ASCII characters have code points in the range U+0000-U+007F. Empty string is ASCII too
print(str1.isascii())  # True
str1 = 'Hello'
str2 = 'Hello world'

print(str1.split())  # ['Hello']
print(str2.split())  # ['Hello', 'world']
print(list(str1))  # ['H', 'e', 'l', 'l', 'o']
print(str1.split('l'))  # ['He', '', 'o']
print(str1.split('l', 1))  # ['He', 'lo']
print(str1.rsplit('l', 1))  # ['Hel', 'o']
print(str1.split('ll'))  # ['He', 'o']

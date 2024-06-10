x = 0
while x < 2:
    print(f'x = {x}')
    x += 1
else:  # Will be executed because no break in for loop
    print("No break")

y = 0
while y < 2:
    print(f'y = {y}')
    y += 1
    break
else:  # Will not be executed because of break in for loop
    print("No break")

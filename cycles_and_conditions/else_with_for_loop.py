for i in range(1, 4):
    print(i)
else:  # Will be executed because no break in for loop
    print("No break")


for i in range(1, 4):
    print(i)
    break
else:  # Will not be executed because of break in for loop
    print("No break")

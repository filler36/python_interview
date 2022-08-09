for i in range(1, 4):
    print(i)
else:  # Executed because no break in for loop
    print("No break")


for i in range(1, 4):
    print(i)
    break
else:  # Will not executed because of break in for loop
    print("No break")

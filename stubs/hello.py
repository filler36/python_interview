def hello(name):
    print("Hello " + str(name))

hello('John')
hello(606)  # IDE will highlight "Expected type 'str', got 'int' instead"

# However, the code will work in both cases, because Python doesn't care about type checking

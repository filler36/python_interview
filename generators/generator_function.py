def get_list():
    for x in range(2):
        yield x  # yield will return x and state of function will be frozen
        print('after yield')  # This statement will not be executed at the first next call


lst = get_list()

print(type(lst))  # <class 'generator'>

print(next(lst))  # 0
print(next(lst))  # Firstly 'after yield' will be printed and only then 1 will be yielded
try:
    print(next(lst))  # 'after yield' will be printed and then StopIteration will be raised
except StopIteration as e:
    # traceback.print_exc()  # Will print out full traceback
    # print(repr(e))  # Will print error type (StopIteration)
    pass

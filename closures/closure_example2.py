"""
With closure, you also can implement a counter for function calls.
"""

def function_with_counter():
    count = 0

    def some_function(msg):
        nonlocal count
        count += 1
        print(f'{count:4}: {msg}')

    return some_function

print_with_counter = function_with_counter()
print_with_counter('Hello')  # 1: Hello
print_with_counter('I count my calls')  # 2: I count my calls


"""
It's worth noting that the details of __closure__ are undocumented and an implementation-specific feature of the CPython implementation
"""
print(print_with_counter.__closure__[0].cell_contents)  # 2

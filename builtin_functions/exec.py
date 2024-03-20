"""
The exec function in Python is used to execute a block of Python code, which can consist of multiple statements or expressions.
It does not return a value like eval.
It takes a single argument, which is a string containing the Python code to be executed.
exec is often used for running dynamically generated Python code, like scripts or code generated at runtime.
"""


# This example shows that exec return None
code = '2 + 2'
result = exec(code)  # exec function always returns None
print(result)  # None


# This example shows executing multiple statements or expressions
code = """
x = 2
y = 2
result = x + y
print(result)
"""
exec(code)  # 4


# This example shows that exec runs code in the same environment
# and has access to the same variables, modules, and namespaces as the rest of your program.
x = 5
code = "x = x + 10"
exec(code)
print(x)  # Output: 15

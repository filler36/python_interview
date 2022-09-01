# Actually, a concise rule for Python Scope resolution, from Learning Python, 3rd. Ed..
# These rules are specific to variable names, not attributes. If you reference it without a period, these rules apply

# LEGB Rule
# Local — Names assigned in any way within a function (def or lambda), and not declared global in that function
# Enclosing-function — Names assigned in the local scope of any and all statically enclosing functions (def or lambda), from inner to outer
# Global (module) — Names assigned at the top-level of a module file, or by executing a global statement in a def within the file
# Built-in (Python) — Names preassigned in the built-in names module: open, range, SyntaxError, etc

#(dir(__builtins__))  # Built-in
#vars = 1  # Global

def somefunc1():
    #vars = 2  # Enclosing
    def somefunc2():
        #vars = 3  # Local
        print(vars)
    somefunc2()

somefunc1()

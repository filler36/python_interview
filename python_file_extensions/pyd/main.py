"""
When you use the cythonize command, Cython does several things.
Cython is a static compiler that translates Python code into C or C++ code.
The .c file: Cython first translates your Python code (.py file) into equivalent C code (.c file).
This C code will look very different from your Python code because it has been translated into a different programming language.
The .pyd file: Cython then compiles this C code into a Python extension module
(.pyd file, equivalent to .so file on Unix/Linux platform), which can be imported and used in other Python scripts just like any other module.
So the .c file is an intermediate product of cythonize process, the last product is .pyd file which is a ready-to-use module in python.
The advantage of using Cython is that it can significantly speed up your Python code,
especially if your code involves tight loops or heavy computations.
By translating Python into C, Cython allows you to bypass the Python interpreter,
and this can lead to significant speedups. Moreover, it allows Python code to call C/C++ code, so we can use powerful C/C++ libraries directly in Python.


If we run `python main.py` when before original_module was cythonized we will see the next output:
    <path_to_the_module>\original_module.py
    Hello World!

After we cythonize the original_module.py with the next command `cythonize -i original_module.py`
and run the main module again we will get the next output:
    <path_to_the_module>\original_module.cp311-win_amd64.pyd
    Hello World!
"""
import original_module

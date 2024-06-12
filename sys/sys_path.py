"""
sys.path is a built-in variable within the sys module.
It contains a list of directories that the interpreter will search in for the required module.

When a module(a module is a python file) is imported within a Python file, the interpreter first searches for the specified module among its built-in modules.
If not found it looks through the list of directories(a directory is a folder that contains related modules) defined by sys.path.

DEFAULT - By default, the interpreter looks for a module within the current directory.
To make the interpreter search in some other directory you just simply have to change the current directory.

PYTHONPATH - You can set this environment variable and python will add path from PYTHONPATH env var to sys.path after CWD

SYS.PATH.APPEND - sys.path.append('C:/some_directory') will append 'C:/some_directory' at the end of sys.path
"""
import sys

print(*sys.path, sep='\n')
print('---')
sys.path.append('C:/some_directory')
print(*sys.path, sep='\n')

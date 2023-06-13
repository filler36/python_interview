import sys

'''
In Python, sys.stdout refers to the standard output stream, which is the default destination for the output
of the print() function and other similar functions. It is a predefined file-like object that represents the screen
or console where the program's output is displayed.

By default, sys.stdout points to the console, but it can be redirected to other destinations
such as a file or another stream.
This can be done by assigning a different file object or stream to sys.stdout.
For example, you can redirect the output to a file by opening a file in write mode and assigning it to sys.stdout:
'''

with open("output.txt", "w") as fp:
    sys.stdout = fp
    print("This will be written to the file.")

"""
All of the statements below will automatically execute __init__.py in package_example2, but only for one time
"""
import package_example2
#import package_example2.file1
#from package_example2 import file1
#from package_example2.file1 import a
print(package_example2.file1.__name__)  # __name__ == package_example2.file1
print(package_example2.a)

try:
    print(package_example2.b)  # This will cause AttributeError because 'b' is not in the __all__
except AttributeError as ex:
    print(ex)
"""
All of the statements below will automatically execute __init__.py in package_sample, but only for one time
"""
import package_sample
#import package_sample.file1
#from package_sample import file1
#from package_sample.file1 import a

print(package_sample.a)

try:
    print(package_sample.b)  # This will cause AttributeError because 'b' is not in the __all__
except AttributeError as ex:
    print(ex)
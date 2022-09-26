print(__name__)

# From: https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time

# If a module's name has no dots, it is not considered to be part of a package.
# It doesn't matter where the file actually is on disk.
# All that matters is what its name is, and its name depends on how you loaded it.
# Top-level scripts CAN'T import relative
# This import will give error if module_a.py will be executed as top-level script because __name__ will be '__main__'
try:
    from .subpackage import module_b
except ImportError as ex:
    print(repr(ex))

# If you really do want to run module_a directly, but you still want it to be considered part of a package, you can do
# python -m package_example1.module_a. The -m tells Python to load it as a module, not as the top-level script.

# Or you can import module_a into main.py and run main.py directly. In that case relative imports in module_a will work

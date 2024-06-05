print(__name__)  # top-level script or python -m -> '__main__'  /  main.py -> 'package_example1.subpackage.module_b'
print(__package__)  # top-level script -> None  /  main.py or python -m -> package_example1.subpackage

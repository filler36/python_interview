import os
import sys
import atexit

"""
Functions that are registered are automatically executed upon interpreter termination.
Whenever a program is killed by a signal not handled by Python, when os.exit() is called,
or Python fatal internal error is detected, the functions registered via this module are not executed.
"""


@atexit.register
def goodbye():
    print('Goodbye!')


def hello():
    print('Hello!')


if __name__ == '__main__':
    hello()
    # exit()  # goodbye will be executed
    # sys.exit()  # goodbye will be executed
    # raise Exception  # goodbye will be executed
    # os._exit(0)  # goodbye will be executed
    # os._exit(1)  # goodbye will NOT be executed

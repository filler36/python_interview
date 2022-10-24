import atexit

@atexit.register
def goodbye():
    print('Goodbye!')

@atexit.register
def hello():
    print('Hello!')

if __name__ == '__main__':
    hello()
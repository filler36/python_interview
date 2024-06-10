class LoggerDecorator:
    def __init__(self, function):
        self.__function = function

    def __call__(self, *args, **kwargs):
        print('Before original function execution')
        result = self.__function(*args, **kwargs)
        print('After original function execution')
        return result


@LoggerDecorator
def hello(text):
    print(f'Hello {text}')


hello('World!')

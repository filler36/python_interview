"""
Closures can be helpful when you need to create a pattern for some function and then call it.
"""


def format_message(format_string):
    frmt_string = format_string

    def inner_function(message):
        print(frmt_string.format(message))

    return inner_function

my_formatter1 = format_message('my formatter 1: {}')
my_formatter1('Hello!')  # my formatter 1: Hello!
my_formatter1('My name is Tom')  # my formatter 1: My name is Tom

my_formatter2 = format_message('my formatter 2: {}')  # my formatter 2: Bye!
my_formatter2('Bye!')

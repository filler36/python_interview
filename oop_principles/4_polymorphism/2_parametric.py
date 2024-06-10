"""
This is an example of "Parametric Polymorphism", sometimes referred to as "Generics" in other languages.

Parametric polymorphism allows a function or a data type to be written generically, so that it can handle values identically without depending on their type.

Python is dynamically typed, which means that variable types are determined and checked at runtime rather than during compilation.
It means that is not necessary to hint argument types of the function in Python. By default, the argument can be of any type.

In your example, you're using Python's typing.TypeVar to define a type variable T.
Then, you’re using T as an annotation for the argument to the print_item function, which means print_item can accept any type of value,
and within the function, the value can be handled irrespective of its type.

When print_item is called with an integer or a string, it works with both types because it's been defined to be polymorphic and can take any type.
It applies the same operation (print) regardless of the actual type of the data.
"""
from typing import TypeVar

T = TypeVar('T')


def print_item(item: T):
    print(item)


print_item(42)         # Works with integers
print_item("Hello")    # Works with strings


"""
In statically typed languages like Java you should define argument type.
So if you want that your function take argument of different type you should use Generics

public class Main {
    public static void main(String[] args) {
        printItem(42);        // Works with integers
        printItem("Hello");   // Works with strings
    }

    public static <T> void printItem(T item) {
        System.out.println(item);
    }
}

This also can be accomplished via function overloading
public class Main {
    public static void main(String[] args) {
        printItem(42);        // Works with integers
        printItem("Hello");   // Works with strings
    }

    public static <T> void printItem(T item) {
        System.out.println(item);
    }
}
"""
"""
Ad-hoc polymorphism, often referred to as "function overloading" or "operator overloading," is a type of polymorphism
where different functions with the same name are invoked based on the arguments they are given.
The function that gets executed is determined by the number and/or types of the arguments.

Here's a breakdown:

Function Overloading: This is when multiple functions with the same name exist in the same scope but have different
parameters (either a different number of parameters or different types). Example in C++:

int add(int a, int b){
  return a + b;
}
double add(double a, double b) {
  return a + b;
}
Here, the function add is overloaded: one version handles integers, and the other handles doubles.


Operator Overloading: Some languages allow operators (like +, -, *, etc.) to be redefined for user-defined types.
This is a form of ad-hoc polymorphism. Example in C++ with a hypothetical Vector class:

Vector operator+(const Vector& v1, const Vector& v2) {
  return Vector(v1.x + v2.x, v1.y + v2.y);
}
Here, the + operator is overloaded to add two Vector objects.
"""




"""
This form of polymorphism is called "Operator Overloading Polymorphism".

In Python, special methods are used to overload operators. These special methods are implicitly called when associated operations are invoked on objects.

For example, the __add__ method in your code is a special method that Python recognizes as corresponding to the addition operator (+).
By defining it in the "Vector" class, you're telling Python how to execute the "+" operator for two objects of the class "Vector".
This is why the operation "v1 + v2" works even though v1 and v2 are custom class objects, not built-in types.

So you can say, in this context, "+" operator can perform addition on integers, concatenate strings and add vectors here,
depending on the data type (or the class definition), illustrating polymorphism.
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Calls the __add__ method, resulting in v3 = Vector(4, 6)

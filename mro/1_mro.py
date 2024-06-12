"""
In Python, the MRO is from bottom to top and left to right.
This means that, first, the method is searched in the class of the object.
If it’s not found, it is searched in the immediate super class.
In the case of multiple super classes, it is searched left to right, in the order by which was declared by the developer

You can determine MRO of the object via accessing __mro__ attribute.
"""
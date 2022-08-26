lst = ['a', 'b', 'c', 'd']

# lst implementation under the hood is just another list of references to the elements of original lst
# Each reference has the same memory size, so we can efficiently O(1) get items by index
lst_implementation = [
    '<reference for the a>',
    '<reference for the b>',
    '<reference for the c>',
    '<reference for the d>'
]

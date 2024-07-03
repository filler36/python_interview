"""
This is implementation-specific, but interpreter is probably interning compile-time constants but not the results of run-time expressions.
The expression "strin"+"g" is evaluated at compile time, and is replaced with "string".

If we examine the bytecodes, we'll see that they are exactly the same:

  # s1 = "string"
  1           0 LOAD_CONST               0 ('string')
              2 STORE_NAME               0 (s1)

  # s2 = "strin" + "g"
  2           4 LOAD_CONST               0 ('string')
              6 STORE_NAME               1 (s2)
"""

s1 = 'string'
s2 = 'strin' + 'g'

print(s1 is s2)  # True

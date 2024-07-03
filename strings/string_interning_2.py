"""
  0           0 RESUME                   0

  1           2 LOAD_CONST               0 ('string')
              4 STORE_NAME               0 (s1)

  2           6 LOAD_CONST               1 ('strin')
              8 STORE_NAME               1 (s2)

  3          10 LOAD_NAME                0 (s1)
             12 LOAD_NAME                1 (s2)
             14 LOAD_CONST               2 ('g')
             16 BINARY_OP                0 (+)
             20 IS_OP                    0
             22 POP_TOP
             24 LOAD_CONST               3 (None)
             26 RETURN_VALUE
"""

s1 = 'string'
s2 = 'strin'
print(s1 is s2 + 'g')  # False

# This Python code assigns the name x to the value 666
x = 666
# Under the hood:
# 1. A PyObject is created in memory
# 2. PyObject type is set to integer
# 3. PyObject value is set to 666
# 4. A name x is created
# 5. x is set to point to the PyObject
# 6. PyObject reference count is set to 1
# -------------          -----------------------------
# Python name |--------> |         PyObject 1        |
# -------------          |-----------------|---------|
#      x      |          | Type            | integer |
# -------------          |-----------------|---------|
#                        | Value           | 666     |
#                        |-----------------|---------|
#                        | Reference Count | 1       |
#                        -----------------------------


x = 667
# Under the hood:
# 1. A new PyObject has to be created because integers are immutable
# 2. The x name points to the new PyObject
# 3. Reference count for the first PyObject will be set to 0. It means that the garbage collector
# can delete that first PyObject
# -------------          -----------------------------
# Python name |--------> |         PyObject 2        |
# -------------          |-----------------|---------|
#      x      |          | Type            | integer |
# -------------          |-----------------|---------|
#                        | Value           | 667     |
#                        |-----------------|---------|
#                        | Reference Count | 1       |
#                        -----------------------------


y = x
# Under the hood:
# 1. A new name y is created and pointed to the same PyObject as x
# 2. Reference count will increase by 1
# -------------          -----------------------------
# Python name |--------> |         PyObject 2        |
# -------------    ,---> |-----------------|---------|
#      x      |    |     | Type            | integer |
# -------------    |     |-----------------|---------|
#                  |     | Value           | 667     |
# -------------    |     |-----------------|---------|
# Python name |----'     | Reference Count | 2       |
# -------------          -----------------------------
#      y      |
# -------------
print(y is x)  # True, because both names points to the same PyObject


y += 1
# Under the hood:
# 1. A new PyObject has to be created because integers are immutable
# 2. Reference count of PyObject 2 will be decreased by 1, because y will not point anymore on the PyObject 2
# 3. Reference count of the new PyObject will be increased by 1
# -------------          -----------------------------
# Python name |--------> |         PyObject 3        |
# -------------          |-----------------|---------|
#      y      |          | Type            | integer |
# -------------          |-----------------|---------|
#                        | Value           | 668     |
#                        |-----------------|---------|
#                        | Reference Count | 1       |
#                        -----------------------------
print(y is x)  # False, because y now points to the new PyObject

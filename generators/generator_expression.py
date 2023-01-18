import traceback

gen = (x for x in range(2))  # Create generator using generator expression
print(type(gen))  # <class 'generator'>
print(next(gen))  # 0
print(next(gen))  # 1
try:
    print(next(gen))  # Will raise StopIteration error
except StopIteration as e:
    #traceback.print_exc()  # Will print out full traceback
    #print(repr(e))  # Will print error type (StopIteration)
    pass

for i in gen:
    print(i)  # Will print nothing, because we can iterate over generator only once

gen = (x for x in range(2))  # Create generator again
for i in gen:
    print(i)  # Now we can iterate through the generator one more time

gen = (x for x in range(1000000000000))  # Generator doesn't keep all the values inside, it just generates it
lst = list(x for x in range(1000000000000))  # Instead of generator the list will keep all values in memory that will lead to memory overflow
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


infinite_sequence_generator = infinite_sequence()
print(type(infinite_sequence_generator))  # <class 'generator'>
for i in infinite_sequence_generator:
    print(i)

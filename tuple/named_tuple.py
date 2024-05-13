from collections import namedtuple

# Define a namedtuple type 'Person' with fields 'name' and 'age'
Person = namedtuple('Person', ['name', 'age', 'country'])

# Create an instance of Person
bob = Person(name="Bob", age=30, country='USA')

print(bob)  # Person(name='Bob', age=30)

# Access fields using keys
print(bob.name)  # Bob

# Access fields using indexes
print(bob[1])  # 30

# Access fields using getattr
print(getattr(bob, 'country'))  # USA

# Access fields using iteration
for i in bob:
    print(i)  # Bob
              # 30
              # USA

# Get named tuple as dict
print(bob._asdict())  # {'name': 'Filip', 'age': '30', 'country': 'Finland'}

# Make NamedTuple from list
filip_list = ['Filip', '30', 'Finland']
filip = Person._make(filip_list)
print(filip)  # Person(name='Filip', age='30', country='Finland')


bob.age = 12  # AttributeError: can't set attribute


from collections import Counter

t = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
d1 = {}
for i in t:
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 1

print(d1)  # {1: 1, 2: 2, 3: 3, 4: 4}

c = Counter(t)
print(c)  # Counter({4: 4, 3: 3, 2: 2, 1: 1})
print(dict(c))  # {1: 1, 2: 2, 3: 3, 4: 4}

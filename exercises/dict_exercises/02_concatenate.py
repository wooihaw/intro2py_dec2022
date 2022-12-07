# Write a Python script to concatenate following dictionaries to create a new one.
# Expected Result: 
# d4 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

d1 = {'a': 10, 'b': 20}
d2 = {'c': 30, 'd': 40}
d3 = {'e': 50}

# Solution 1
d4_1 = {}
for d in (d1, d2, d3):
    for k in d:
        d4_1[k] = d[k]
print(f'{d4_1=}')

# Solution 2
d4_2 = {k: d[k] for d in (d1, d2, d3) for k in d}
print(f'{d4_2=}')

# Solution 3
d4_3 = {}
for d in (d1, d2, d3):
    d4_3.update(d)
print(f'{d4_3=}')


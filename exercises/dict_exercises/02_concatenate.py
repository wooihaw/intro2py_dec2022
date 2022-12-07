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
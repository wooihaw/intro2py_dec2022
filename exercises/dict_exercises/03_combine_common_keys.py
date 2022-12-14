# Write a Python program to combine two dictionary adding values for common keys.
# Expected output: d3 = {'a': 400, 'b': 400, 'c': 300, 'd': 350}

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':350}

# Solution 1
d3_1 = {}
for d in (d1, d2):
    for k in d:
        if k in d1 and k in d2:
            d3_1[k] = d1[k] + d2[k]
        elif k in d1:
            d3_1[k] = d1[k]
        elif k in d2:
            d3_1[k] = d2[k]
print(f'{d3_1=}')

# Solution 2
d3_2 = d1.copy()
for k in d2:
    if k in d3_2:
        d3_2[k] = d2[k] + d3_2[k]
    else:
        d3_2[k] = d2[k]
print(f'{d3_2=}')
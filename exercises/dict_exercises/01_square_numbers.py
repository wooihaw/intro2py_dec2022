# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
# Expected results:
# square =  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# Solution 1
square1 = {}
for i in range(1, 16):
    square1[i] = i*i
print(f'{square1=}')

# Solution 2
square2 = {i: i*i for i in range(1, 16)}
print(f'{square2=}')

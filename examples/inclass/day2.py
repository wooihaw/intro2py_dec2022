# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:24:33 2022

@author: wooihaw
"""
#%% Using get() method for dictionary
adict = dict(a=1, b=2)
# print(adict['c'])  # KeyError as the key 'c' cannot be found
print(adict.get('c', 'Not found'))

print(adict.setdefault('d', 4))
print(f'{adict=}')

#%% Different between del and pop() method
adict = dict(a=1, b=2, c=3)
print(f'{adict=}')

del adict['b']
print(f'{adict=}')

d = adict.pop('c')
print(f'{adict=}')
print(f'{d=}')

#%% Ask user to insert key-value pairs into dictionary
adict = {}
kv = input("Enter key value pair separated by comma: ")
k, v = kv.split(',')
adict[k] = float(v)
print(f'{adict=}')

#%% Joining 2 dictionaries
d1 = dict(a=1, b=2)
d2 = dict(x=3, y=4, z=5)

d1.update(d2)
print(f'{d1=}')  # join d2 into d1

d1['a'] = -1
print(f'{d1=}')  # update the value for 'a'

d3 = dict(b=0)
d1.update(d3)
print(f'{d1=}')  # on;y update the value for 'b'

#%% Set examples
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
s2 = {1, 3, 5, 7, 9}
s3 = {2, 4, 6, 8, 10}

print(f'{s1-s3=}')  # return the items in s1 that are not in s3
print(f'{s3-s1=}')  # return the items in s3 that are not in s1
print(f'{s1.symmetric_difference(s3)=}')  # return items not in both s1 and s3
print(f'{s3.symmetric_difference(s1)=}')  # return items not in both s1 and s3

#%% Set will remove duplicated items
alist = [1, 3, 2, 1, 1, 3, 4, 'abc', 5, 'abc']
print(f'{set(alist)=}')

#%% Empty sequences are treated as Falase, otherwise they are treated as True
alist = []
print('Not empty' if alist else 'Empty')

alist.append(0)
print('Not empty' if alist else 'Empty')

adict = {}
print('Not empty' if adict else 'Empty')

adict['a'] = 123
print('Not empty' if adict else 'Empty')

#%% Iterate through more than one lists in a for loop
fruits = ['apples', 'orange', 'pear']
prices = [1.5, 2.5, 4]

# Using range() to generate a sequence of numbers to be used as index
for i in range(len(fruits)):
    print(f'{fruits[i]}: {prices[i]}')
    
# Alternatively, zip() can be used to combined the lists
for i, j in zip(fruits, prices):
    print(f'{i}: {j}')

#%% List comprehension example 1
names = ['ali', 'bala', 'chen', 'david']

# Using for loop
cap_names1 = []
for n in names:
    cap_names1.append(n.capitalize())
print(f'{cap_names1=}')

# Using list comprehension
cap_names2 = [n.capitalize() for n in names]
print(f'{cap_names2=}')

#%% List comprehension example 2
alist = ['Java', 'Rust', 'Python', 'Swift', 'Go']

# Using for loop
filtered_list1 = []
for i in alist:
    if 'o' in i:
        filtered_list1.append(i)
print(f'{filtered_list1=}')

# Using list comprehension
filtered_list2 = [i for i in alist if 'o' in i]
print(f'{filtered_list2=}')

#%% List comprehension example 3
s = 'Testing 123! Are you there?'

# Using for loop
t1 = []
for c in s:
    t1.append(c if c.isalpha() else ' ')
u1 = ''.join(t1)
w1 = u1.split()
print(f'{w1=}')

# Using list comprehension
t2 = [c if c.isalpha() else ' ' for c in s]
u2 = ''.join(t2)
w2 = u2.split()
print(f'{w2=}')

#%% Dictionary comprehension
fruits = ['apples', 'orange', 'pear']
prices = [1.5, 2.5, 4]

inventory = {k: v for k, v in zip(fruits, prices)}
print(f'{inventory=}')

# Using for loop
discount_inventory1 = {}
for k in inventory:
    discount_inventory1[k] = 0.9*inventory[k]
print(f'{discount_inventory1=}')

# Using dictionary comprehension to generate a dictionry for 10% discount
discount_inventory2 = {k: 0.9*inventory[k] for k in inventory}
print(f'{discount_inventory2=}')















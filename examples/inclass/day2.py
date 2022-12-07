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





















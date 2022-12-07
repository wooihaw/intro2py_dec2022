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




















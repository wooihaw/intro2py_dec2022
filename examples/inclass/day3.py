# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 09:28:43 2022

@author: wooihaw
"""
#%% Function example 1
def add_one(x):
    print(x + 1)

add_one(5)
x = add_one(3)
print(f'{x=}')

alist = [3, 1, 2]
blist = alist.sort()
clist = sorted(alist)
print(f'{alist=}')
print(f'{blist=}')
print(f'{clist=}')

#%% Function Example 2
def myfunc(a, b, c=3):
    print(f'{a=}, {b=}, {c=}')

myfunc(2, 1, 5)
myfunc(3, b=6)
#myfunc(a=1, 4, 7)  # Not allowed

#%% Using lambda function with sorted()

alist = ['ID12', 'ID3', 'ID57', 'ID101', 'ID85', 'ID1']
blist = sorted(alist)
print(f'{blist=}')

clist = sorted(alist, key=lambda x:int(x[2:]))
print(f'{clist=}')

















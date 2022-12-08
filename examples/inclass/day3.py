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

#%% Using lambda function with max()

paper_size = ('A1', 'A4', 'A3', 'A5', 'A2')

print(f'{max(paper_size)=}')

print(f'{max(paper_size, key=lambda x:-int(x[1:]))=}')

print(f'{min(paper_size, key=lambda x:-int(x[1:]))=}')

#%% Using map() with lambda function

# Using list comprehension
sqr1 = [x*x for x in range(1, 11)]

# Using map() with lambda function
sqr2 = list(map(lambda x: x*x, range(1, 11)))

print(f'{sqr1=}')
print(f'{sqr2=}')

#%% Using filter() with lambda function

# Using list comprehension
odd1 = [x for x in range(10) if x%2]

# Using filter() with lambda function
odd2 = list(filter(lambda y: y%2, range(10)))

print(f'{odd1=}', f'{odd2=}', sep='\n')






























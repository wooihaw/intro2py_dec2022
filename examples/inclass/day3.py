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
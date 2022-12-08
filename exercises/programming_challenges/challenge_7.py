# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:40:53 2022

@author: wooihaw
"""
#Using map() and filter()
sqr1 = list(map(lambda x:x*x, filter(lambda y:y%2==0, range(1, 101))))
print(f"{sqr1=}")

# Using list comprehension
sqr2 = [x*x for x in range(1, 101) if x%2==0]
print(f"{sqr2=}")

# Using for loop
sqr3 = []
for x in range(1, 101):
    if x%2==0:
        sqr3.append(x*x)
print(f"{sqr3=}")
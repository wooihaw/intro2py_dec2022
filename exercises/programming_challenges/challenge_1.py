# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:30:59 2022

@author: wooihaw
"""
# Challenge 1
# c -> number of chickens
# r -> number of rabbits
# c + r = 35
# 2*c + 4*r = 94

for c in range(36):
    r = 35 - c
    if 2*c + 4*r == 94:
        print(f'There are {c} chickens and {r} rabbits.')

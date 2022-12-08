# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:49:34 2022

@author: wooihaw
"""
s1 = set(range(1, 101))
s2 = set(range(5, 101, 5))
s3 = set(range(7, 101, 7))

results = s1 - (s2 | s3)
print(results)
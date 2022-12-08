# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:05:34 2022

@author: wooihaw
"""

def median(items: list) -> float:
    n = len(items)
    if n%2 == 1:
        return items[n//2]
    else:
        return (items[n//2 - 1] + items[n//2]) / 2

with open('data/Heathrow.txt', 'r') as f:
    raw_data = f.readlines()
    data = [float(s.strip()) for s in raw_data]
    
    data.sort()
    minimum, maximum = data[0], data[-1]
    
    mean = sum(data)/len(data)
    med = median(data)
    
    print(f"{minimum=}, {maximum=}, {mean=}, {med=}")
    
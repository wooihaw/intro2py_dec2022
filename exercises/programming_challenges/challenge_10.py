# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 17:00:15 2022

@author: wooihaw
"""
from collections import Counter

with open('data/alice.txt', 'r') as f:
    s = f.read()
    t = [c.lower() if c.isalpha() else ' ' for c in s] # replace non-alphabet with space
    w = ''.join(t).split()  # w is the list of all words
    
    c = Counter(w)
    print(f"Top 10 most frequent words: {c.most_common(10)}")
    print(f"The word 'alice' appears {c['alice']} in the text.")
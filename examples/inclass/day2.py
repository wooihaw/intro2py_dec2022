# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:24:33 2022

@author: wooihaw
"""
#%% Using get() method for dictionary
adict = dict(a=1, b=2)
# print(adict['c'])  # KeyError as the key 'c' cannot be found
print(adict.get('c', 'Not found'))

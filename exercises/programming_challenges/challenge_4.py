# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:55:07 2022

@author: wooihaw
"""
name_age = {}
for i in range(3):
    name = input(f"Enter name of person {i+1}: ")
    age = input(f"Enter age of person {i+1}: ")
    name_age[name] = age

name = input("Enter a name: ")
print(f"{name}'s age is {name_age.get(name, 'unknown')}")
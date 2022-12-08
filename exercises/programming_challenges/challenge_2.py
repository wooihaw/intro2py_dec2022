# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:37:34 2022

@author: wooihaw
"""

try:
    investment = float(input("Enter the initial investment: "))
    rate = float(input("Enter the annual rate: "))
    years = int(input("Enter the year of investment: "))
except Exception as e:
    print(f"Error: {e}")
else:
    print(f"Initial investment: ${investment}, annual rate: {rate}%, years of investment: {years}")
    for i in range(years):
        investment += investment * rate/100
        print(f"Year {i+1}: ${investment:.2f}")
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:27:08 2022

@author: wooihaw
"""
def convert_cel_to_far(c: float) -> float:
    return c * 9/5 + 32

def convert_far_to_cel(f: float) -> float:
    return (f - 32) * 5/9

try:
    far = float(input("Enter a temperature in Fahrenheit: "))
    cel = float(input("Enter a temperature in Celsius: "))
except Exception as e:
    print(f"Error: {e}")
else:
    print(f"{far:>8.2f}{0x00b0:c}F -> {convert_far_to_cel(far):.2f}{0x00b0:c}C")
    print(f"{cel:>8.2f}{0x00b0:c}C -> {convert_cel_to_far(cel):.2f}{0x00b0:c}F")
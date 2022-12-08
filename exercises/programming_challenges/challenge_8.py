# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:47:21 2022

@author: wooihaw
"""
class Circle:
    pi = 3.141592653589793
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return Circle.pi * self.radius ** 2
    def circumference(self):
        return 2 * Circle.pi * self.radius
    
if __name__ == "__main__":
    c1 = Circle(4)
    print(f"Area: {c1.area():.2f}, circumference: {c1.circumference():.2f}")
    c2 = Circle(7)
    print(f"Area: {c2.area():.2f}, circumference: {c2.circumference():.2f}")
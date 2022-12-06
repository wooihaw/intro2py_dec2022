# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 12:14:38 2022

@author: wooihaw
"""

#%% Check size of variable
a = 1234567890
print(a.__sizeof__())

#%% Binary and hexadecimal numbers
a = 0b10110001
b = 0x123def
c = a + b

print(a, b, c, sep=',')
print(hex(a))
print(bin(b))

#%% Do not begin a variable name with a digit
# 1star = 12345  # This will cause a syntax error
_1star = 12345  # instead we can start with an underscore

#%% Converting from one data type to another
a, b, c = 1, 2.3, 'abc'

d = float(a)
e = int(b)
f = int(c, base=16)  # Treating c as a hexadecimal number

print(a, b, c, d, e, f, sep=',')

x = '12345'
y = int(x)
print(x, y, sep=',')

g = str(a)
# h = g + 1  # string cannot be added with an integer

#%% Arithmetic operators have different priorities
a = 2**2
b = -2**2
print(a, b, sep='\n')

c = (-2)**2
print(c)

#%% Comparison operators will return either True or False
a = 10
b = 25
print(a < b)
print(a > b)
print(a == b)
print(a != b)

print(0 <= a < 20)
print(0 <= b < 20)

#%% Mixing single quotes and double quotes in strings
s1 = "It's a python."
s2 = 'John said "Yes, I am the one.".'
print(s1, s2, sep='\n')

s3 = 'It\'s a python.'
print(s3)

#%% Multiline string
s4 = '''This is a multiline
string that spans multiple
lines.'''
s5 = """This is another multiline
string that spans multiple
lines."""
print(s4, s5, sep='\n')

#%% String slicing examples
s = 'apple pie'
print(s[2:-2])
print(s[-2:2])  # Not working since the default step is 1
print(s[-2:2:-1])  # Works by change the step to -1

#%% String concatenation and repetition
s = 'hello'
t = 'c' + s[1:]
print(s, t, sep='\n')

print('=' * 40)
print('This is a new section.')
print(5 * 'Ha ')

#%% More string methods
m = 'Hello, World!'
print(m.swapcase())
print(m.split())
print(m.replace('l', ''))  # remove all 'l'
print(m.replace('l', '', 1))  # only remove the first 'l'
print(m)

n = 'abc123'
print(n.isalpha())
print(n.isdigit())
print(n.isalnum())

p = '    This is a string.   \n'
print(p)
print(p.lstrip())
print(p.rstrip())
print(p.strip())

q = '    This is a string.   \n   abc'
r = q.split('\n')
print(r)
print(r[0].strip())
print(r[1].strip())

s = r[0].strip() + r[1].strip()
print(s)

print('The character "l" appears ' + str(m.count('l')) + ' times')
print(f'The character "l" appears {m.count("l")} times')
















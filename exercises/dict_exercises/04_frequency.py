# Write a Python script to find the frequency of occurance for each alphabet in a string.
astring = 'The quick brown fox jumps over the lazy dog.'

# Clean and normalize the text
alist = [c.lower() for c in astring if c.isalpha()]
print(f'{alist=}')

uniq_alphabets = sorted(set(alist))  # get a list of sorted unique alphabets

freq = {}
for a in uniq_alphabets:
    freq[a] = alist.count(a)
print(f'{freq=}')

# Alternative solution
from collections import Counter

c = Counter(alist)
print(c)
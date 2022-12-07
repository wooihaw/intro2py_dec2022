# Write a Python script to find common items between two lists.
alist = [99, 'P', 1, 'xyz', 'a', 2.5]
blist = ['xyz', 2.5, 2.5, 3, 99, 99, 2.5, 'xyz', -1.2, 99]

# Solution 1
clist1 = list(set(alist) & set(blist))
print(f'List of common items: {clist1}')

# Solution 2
clist2 = []
for i in alist:
    if i in blist:
        clist2.append(i)
print(f'List of common items: {clist2}')
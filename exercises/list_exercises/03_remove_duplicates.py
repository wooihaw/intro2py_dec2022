# Write a Python script to remove duplicates from a list.
alist = [99, 3, -1.2, 2.5, -1.2, -1.2, 5.75, 'xyz', 'a', 99, 'P', 'a', 2.5, 'xyz', 99, 'xyz', 99, 'xyz', 1, -1.2]
print(f'{alist=}')

# Solution 1
print(f'{list(set(alist))}')

# Solution 2
uniq_list = []
for i in alist:
    if i not in uniq_list:
        uniq_list.append(i)
print(f'{uniq_list=}')        
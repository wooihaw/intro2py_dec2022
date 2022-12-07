# Write a Python script to multiply all the items in a list.
alist = [12, 43, 57, 98, 83, -103, 256, -1]
print(f'{alist=}')

a = 0
for i in alist:
    a = a + i
print(f'{a=}')
print(f'{sum(alist)=}')
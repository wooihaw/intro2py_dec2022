# Write a Python script to ask for a number and a thing name, 
# and print a grmmatically correct sentence describing the number of things.
# E.g.
# Enter a number: 5
# Enter a thing name: python
# There are 5 pythons.
#
# Enter a number: 1
# Enter a thing name: apple
# There is 1 apple.

num = input('Enter a number: ')
thing = input('Enter a thing name: ')

if num == '1':
    print(f'There is {num} {thing}.')
else:
    print(f'There are {num} {thing}s.')
    
output = f'There {"is" if num=="1" else "are"} {num} {thing}{"" if num=="1" else "s"}.'
print(output)
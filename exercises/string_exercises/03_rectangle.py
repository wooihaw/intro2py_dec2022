# Write a Python script to ask for the length and width of a rectangle, 
# calculate and print the perimeter and area of the rectangle.
# E.g.
# Enter length: 5
# Enter width: 3
# perimeter = 16, area = 15.

try:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
except:
    print('Invalid input. Please enter number only.')
else:
    perimeter = 2*length + 2*width
    area = length * width
    print(f"{perimeter = }, {area = }")
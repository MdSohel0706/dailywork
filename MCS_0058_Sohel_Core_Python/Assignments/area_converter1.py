"""
Create a program that reads the length and width of a farmer’s field from the user in feet.
Display the area of the field in acres.
"""
length = float(input("Enter the length in feet: "))
width = float(input("Enter the width feet : "))
area_in_feet = length * width
area_in_acres = area_in_feet/43560
print("Area = ",area_in_acres," acres")
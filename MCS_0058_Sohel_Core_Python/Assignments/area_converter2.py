"""
Create a program that reads the length and width of a farmer’s field from the user in feet.
Display the area of the field in acres.
"""
length = float(input("Enter the length in feet: "))
width = float(input("Enter the width feet : "))
area = str(length*width/43560)+" acres"
print("Area = ",area)
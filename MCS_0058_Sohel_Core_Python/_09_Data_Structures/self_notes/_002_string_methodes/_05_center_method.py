print('-----------------------------center--------------------------')
print("The center() method returns a string which is padded with the specified character")

name = 'python'
print("normal string is        :",name)
# print("applying center method  :",name.center())   # TypeError: center expected at least 1 argument, got 0

print("applying center method  :",name.center(20))

print("applying center method  :",name.center(20,'&'))


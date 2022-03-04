#Dictionary:
"""Python is an unordered collection of data values, used to store data
values like a map, which unlike other Data Types that hold only single value as an
element, Dictionary holds key:value pair. Key-value is provided in the dictionary to
make it more optimized. Each key-value pair in a Dictionary is separated by a colon :,
whereas each key is separated by a ‘comma’"""

"""
x = {"name" : "satish", "age" : 36}
#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""

"""# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)"""

"""# with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)"""

"""# with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)"""

"""# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)"""

""" # Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])
# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(3)) """

"""dict ={'Name':'Zara','Age':7,'Class':'First'}
dict['Age']=8;# update existing entry
dict['School']="DPS School";# Add new entry
print"dict['Age']: ", dict['Age']
print"dict['School']: ", dict['School']
"""
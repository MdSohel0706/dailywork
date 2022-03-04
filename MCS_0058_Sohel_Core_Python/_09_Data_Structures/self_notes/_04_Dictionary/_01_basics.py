#Python Dictionary

"""Dictionary in Python is an unordered collection of data values, used to store data
values like a map, which, unlike other Data Types that hold only a single value as an
element, Dictionary holds key:value pair. Key-value is provided in the dictionary to
make it more optimized."""

#Creating a Dictionary

'''In Python, a Dictionary can be created by placing a sequence of elements within curly
{} braces, separated by ‘comma’. Dictionary holds a pair of values, one being the Key
and the other corresponding pair element being its Key:value. '''

'''order_details = [12123321, 2133213, 12323, 'TLEE234e3', 43243, '560036']
e_data = [100, 'Madhu Nettem', 2000003
    , 'Male', 'Bangalore', '560037', ['123', 'area', ]]
# address
print("Employee data : ", e_data)

e_data = {'eid': 100,
          'name': 'Madhu Nettem',
          'sal': 45000,
          'gender': 'Male',
          'loc': 'Bangalore',
          'pin': [1, 2, 3, 4, 5, 6],
          'address': {'hno': '123', 'area': 'marthahalli'}
          }

print("House no :", e_data['address']['hno'])
print("Pin no   :", e_data['pin'][3])

order_details = [123213, 3432, 'Madhu Nettem', 'Bangalore', 543.56, 23, 5, '560037', 4]

order_details = {'order_no': 123213,
                 'ref_no': 3432,
                 'cust_name': 'Madhu Nettem',
                 'del_loc': 'Bangalore',
                 'total_bill': 543.56,
                 'discount': 23,
                 'disc_percnt': 5,
                 'pin_code': '560037',
                 'no_of_items': 4,
                 }

e_ids = {1, 2, 3, 4, 5, 6}
print("Order details : ", order_details)
print("Location : ", order_details['del_loc'])
print("Order No : ", order_details['order_no'])
# print("Order No : ", order_details[100])
'''

'''
Dictionary : 
    - Mutable data structure
    - Unordered
    - Key value pair i.e, items 
    Key properties:
        - Keys must be UNIQUE
        - Keys must be IMMUTABLE and values can be anything

'''
# 1. Keys must be IMMUTABLE and values can be anything
'''dict1 = {100: 10,
         200: {1: 1, 2: 2},
         102.3: 29,
         True: 'Madhu',
         'Message': [1, 2, 3, 4, 5],
         (1, 2, 3): (1, 2, 3),
         # [1,2,3] : {1:1,2:2},  # Wrong, List is mutable
         # {1:1,2:2} : "Hello"   # Wrong, dict is mutable
         # {1,2,3} : "Hello"     # Wrong, set is mutable
         }

print("Keys immutable : ", dict1)
# Dict keys should not be List, Dictionary, Set

# 2. Keys must be unique
x = 10
x = 20

dict1 = {10: 100,
         20: 200,
         10: 150
         }
print("Keys must be unique :", dict1)'''

'''vechical_details = {"AP164567","suziki","speed","Rs600000"}
print("Enter the vechical_details :",vechical_details)'''

employee = {'employee_id': 501,
          'employee_name': 'satish',
          'employee_sal': 28000,
          'employee_gender': 'Male',
          'employee_loc': 'Bangalore',
          'employee_pin': ["521002"],
          'employee_address': {'hno': '123', 'area': 'marthahalli'},
          'employee_address': {"Drno":"265","area": "hyderabad"},
          }
print("Enter the employee id :",employee, type(employee))
print(employee["employee_sal"])
print(employee["employee_gender"])
print(employee["employee_address"])
print(employee["employee_pin"])
print(employee["employee_id"])
del employee["employee_sal"]
del employee["employee_address"]
"""
#DICTIONARY:

1.Python Dictionary is used to store the data in a key-value pair format.
2.dictionary is the data type in Python,
3.which can simulate the real-life data arrangement where some specific value exists for some particular key.
4.It is the mutable data-structure. The dictionary is defined into element Keys and values.

    ==>Keys must be a single element
    ==>Value can be any type such as list, tuple, integer, etc.

5.In other words, we can say that a dictionary is the collection of key-value pairs
where the value can be any Python object.
6.In contrast, the keys are the immutable Python object, i.e., Numbers, string, or tuple.

#Creating the dictionary:

1.The dictionary can be created by using multiple key-value pairs enclosed with the curly brackets {}
and each key is separated from its value by the colon (:)

#Accessing the dictionary values:

1.the values can be accessed in the dictionary by using the keys as keys are unique in the dictionary.

#Adding dictionary values:

1.The dictionary is a mutable data type, and its values can be updated by using the specific keys.
2.The value can be updated along with key Dict[key] = value.
3.The update() method is also used to update an existing value.

Note: If the key-value already present in the dictionary, the value gets updated.
Otherwise, the new keys added in the dictionary.

#Deleting the elements in the dictionary:
1.The items of the dictionary can be deleted by using the del keyword

@Using pop() method:

1.The pop() method accepts the key as an argument and remove the associated value

#Properties of Dictionary keys:

1. In the dictionary, we cannot store multiple values for the same keys.
If we pass more than one value for a single key,
then the value which is last assigned is considered as the value of the key.

2. In python, the key cannot be any mutable object. We can use numbers, strings, or tuples as the key,
but we cannot use any mutable object like the list as the key in the dictionary.

#Removing elements from Dictionary:

1.We can remove a particular item in a dictionary by using the pop() method.
This method removes an item with the provided key and returns the value.

2.The popitem() method can be used to remove and return an arbitrary (key, value) item pair from the dictionary.
All the items can be removed at once, using the clear() method.

3.We can also use the del keyword to remove individual items or the entire dictionary itself.


#Python Dictionary Comprehension:

1.Dictionary comprehension is an elegant and concise way to create a new dictionary
from an iterable in Python.

2.Dictionary comprehension consists of an expression pair (key: value)
followed by a for statement inside curly braces {}.

3.A dictionary comprehension can optionally contain more for or if statements.

4.An optional if statement can filter out items to form the new dictionary


"""
"""
#BUILTIN DICTIONARY FUNCTIONS:

1	cmp(dict1, dict2)
    It compares the items of both the dictionary and returns true
    if the first dictionary values are greater than the second dictionary, otherwise it returns false.

2	len(dict)
    It is used to calculate the length of the dictionary.

3	str(dict)
    It converts the dictionary into the printable string representation.

4	type(variable)
    It is used to print the type of the passed variable.
5.all()
	Return True if all keys of the dictionary are True (or if the dictionary is empty).

6.any()
	Return True if any key of the dictionary is true. If the dictionary is empty, return False.

7.len()
    Return the length (the number of items) in the dictionary.

8.cmp()
	Compares items of two dictionaries. (Not available in Python 3)

9.sorted()
    Return a new sorted list of keys in the dictionary
"""



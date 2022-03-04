
# len()
'''employee_data = {'employee_id': 100,
          'name': 'venkat',
          'sal': 19000,
          'mobile': "8247238634",
          'office': 'hyderabad'
          }

print("Length of dict : ", len(employee_data))

# type()
print("Length of dict : ", type(employee_data))

# str()
di_str = str(employee_data)
print("Dict in string format :", type(di_str), di_str)

# dict()
# di2 = dict({})


# Builtin functions:

employee_data= {'employee': 100,
          'name': 'satish',
          'sal': 18000,
          'mobile': '8247238634',
          'office': 'machiipatnam'
          }

# 1. keys() :To retrieve all keys from dictionary
print("-----------1,. KEYS----------")
d_keys = employee_data.keys()
print("E Data keys : ", d_keys, type(d_keys))
d_keys = list(employee_data.keys())
print("E Data keys : ", d_keys, type(d_keys))

print("-----Dictionary keys ------")
for key in employee_data.keys():   # list(e_data.keys())
    print(key)

print("-----------2. values()----------")
# values() : To retrieve all values from dictionary
d_vals = employee_data.values()
print("E Data values :", d_vals, type(d_vals))
d_vals = list(d_vals)
print("E Data values :", d_vals, type(d_vals))

print("-----Dictionary values ------")
for val in employee_data.values():  # list(e_data.values())
    print(val)


print("-----------3. items() ----------")
# 3. items() : To retrieve all items from dictionary
items = employee_data.items()
print("E DATA Items : ", items, type(items))
items = list(items)
print("E DATA Items : ", items, type(items))


n1, n2 = (1, 2)  # tuple unpacking
print("Values : ", n1, n2)

print("Iterating through dict items")
for item in employee_data.items():
    print(item)

print("-------------------")

for key, val in employee_data.items():
    print(key, " --- ", val)'''


# 4. update()
print("-----------4. update() ----------")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)

dict1 = {1: 1, 2: 2}
dict2 = {3: 3, 4: 4}
dict1.update(dict2)
print("Dictionary Update  : ", dict1, dict2)

print("-----------5. clear() ----------")
di = {1: 1, 2: 2, 3: 3, 4: 4}
print("Before clear : ", di)
di.clear()
print("After clear : ", di)

print("-----------6. fromkeys() ----------")

di = {1: 1, 2: 2}
di = di.fromkeys([10, 20, 30, 40], "Hello")
print("Dictionary from keys : ", di)


print("-----------7. copy() ----------")
di1 = {1: 1, 2: 2}
di2 = di1.copy()
print("-----Before modification-----------")
print("Dict1 copy : ", di1)
print("Dict2 copy : ", di2)
print("-----After modification-----------")
di2['name'] = 'satish'
print("Dict1 copy : ", di1)
print("Dict2 copy : ", di2)

print("-----------8 . has_key() ----------")

dict1 = {1: 1, 2: 2, 'Hello': 'satish'}
'''
print("Has key : ", dict1.has_key('Hello'))
print("Has key : ", dict1.has_key(1))
print("Has key : ", dict1.has_key(10))
'''
'''
pop() popitem() setdefault()
'''

print("-----------8 . get() ----------")

e_data = {'eid': 43256,
          'name': 'satish',
          'sal': 14000,
          'mobile': '8247238634',  # 91-8247238634
          'office': 'hyderabad'
          }
# ecommerce:
xyz = {'orderno': 12123232,
       'ref_no': 324324,
       'items_qty': 4,
       'price': 324324,
       'del_addr': []}

# singup loginpage username password

print("Employee data : ", e_data)
print("Employee name : ", e_data['name'])
print("Employee mobile  : ", e_data['mobile'])
# print("Employee name : ",e_data['company'])  # ERROR
print("Employee company : ", e_data.get('company'))  # to avoid exception
print("Employee company : ", e_data.get('company', 'ORACLE'))  # to set default value if key doesnot exists


print("Employee name : ", e_data.get('name'))
print("Employee name : ", e_data.get('mobile'))
print("Employee name : ", e_data.get('mobile', '----------'))
print("Employee name : ", e_data.get('company'))
print("Employee name : ", e_data.get('company', 'modernchipsolutionspvt  '))

'''Aadhar card info '''

aadhar_deatils = {'a_no': 32423423213678,
                  'name': 'katta satish babu',
                  'email': 'satishbabukatta96@gmail.com',
                  'mobile': '8247238634',
                  'location': 'machilipatnam'
                  }


aadhar_deatils = {'a_no': 32423423213678,
                  'name': 'satish babu',
                  'location': 'machilipatnam'
                  }

'''
Database:
-----------------------------------------------------------------------------
SNo A_NO       NAME         MOBILE       EMAIL                    LOCATION 
-----------------------------------------------------------------------------
11   3243675   satish       8247238634    satishbabukatta96@gmail.com    machilipatanam
11   3243675   satish       null          null                     machilipatanam
------------------------------------------------------------------------------
'''

"""
#PROGRAMS:

1.Python Program to Add a Key-Value Pair to the Dictionary?

key=int(input("Enter the key (int) to be added:"))
value=int(input("Enter the value for the key to be added:"))
d={}
d.update({key:value})
print("Updated dictionary is:")
print(d)

2.Python Program to Concatenate Two Dictionaries Into One?

d1={'A':1,'B':2}
d2={'C':3}
d1.update(d2)
print("Concatenated dictionary is:")
print(d1)

3.Python Program to Check if a Given Key Exists in a Dictionary or Not?

d={'A':1,'B':2,'C':3}
key=raw_input("Enter key to check:")
if key in d.keys():
      print("Key is present and value of the key is:")
      print(d[key])
else:
      print("Key isn't present!")


4.Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)

5.Python Program to Sum All the Items in a Dictionary?

d={'A':100,'B':540,'C':239}
print("Total sum of values in the dictionary:")
print(sum(d.values()))

6.Python Program to Remove the Given Key from a Dictionary?

d = {'a':1,'b':2,'c':3,'d':4}
print("Initial dictionary")
print(d)
key=raw_input("Enter the key to delete(a-d):")
if key in d:
    del d[key]
else:
    print("Key not found!")
    exit(0)
print("Updated dictionary")
print(d)


7.Python Program to Form a Dictionary from an Object of a Class?

class A(object):
     def _init_(self):
         self.A=1
         self.B=2
obj=A()
print(obj._dict_)


8.Python Program to Map Two Lists into a Dictionary?

keys=[]
values=[]
n=int(input("Enter number of elements for dictionary:"))
print("For keys:")
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    keys.append(element)
print("For values:")
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    values.append(element)
d=dict(zip(keys,values))
print("The dictionary is:")
print(d)


9.Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary?

test_string=raw_input("Enter string:")
l=[]
l=test_string.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))


"""
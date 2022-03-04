
order_details = [12123321, 2133213, 12323, 'TLEE234e3', 43243, '560036']
e_data = [100, 'Madhu Nettem', 45000, 'Male', 'Bangalore', '560037',['123','area',]]
# address
print("Employee data : ",e_data)

e_data = {'eid':100,
          'name':'Madhu Nettem',
          'sal':45000,
          'gender':'Male',
          'loc':'Bangalore',
          'pin': [1,2,3,4,5,6],
          'address':{'hno':'123','area':'marthahalli'}
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

e_ids = {1, 2, 3, 4, 5 , 6}
print("Order details : ", order_details)
print("Location : ", order_details['del_loc'])
print("Order No : ", order_details['order_no'])
# print("Order No : ", order_details[100])


'''
Dictionary : 
    - Mutable data structure
    - Unordered
    - Key value pair i.e, item 
    Key properties:
        - Keys must be UNIQUE
        - Keys must be IMMUTABLE and values can be anything
        
'''
# 1. Keys must be IMMUTABLE and values can be anything
dict1 = {100: 10,
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
print("Keys must be unique :", dict1)


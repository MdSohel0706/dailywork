'''
Created on 13-Jun-2021
@author: madhu
'''
'''Below fucntion can be called in 2 ways
 1. By passing one argument only
 1. By passing two argument only
'''
def get_power(voltage, state='MY_STATE'):
    print("Voltage, State : ",voltage,state)

get_power(10)        # Default
get_power(10, "AP")  # Positional
get_power(state='Karnataka', voltage=10)  # keyword
get_power(voltage=10, state='Telangana')  # keyword

print("----------------------------")

def get_power(voltage, state='state', action='action', type='type'):
    print("VOLTAGE = ", voltage)
    print("STATE   = ", state)
    print("ACTION  = ", action)
    print("TYPE    = ", type)
    print("---------------End of method--------------")

'''
Error function calls:
----------------------
get_power(10,action='HELLO',100)    # Positional argument after keyword argument
get_power()                         # required argument missing
get_power(voltage=5.0, 'dead')      # non-keyword argument after a keyword argument
get_power(110, voltage=220)         # duplicate value for the same argument
get_power(110, actor='NTR')         # unknown keyword argument
'''

print("--------# 1 positional argument----------")
get_power(1000)
get_power(1000, 'X')
get_power(1000, 'X', 'Y')
get_power(1000, 'X', 'Y', 'Z')
get_power('a million', 'brief of life', 'jump')
print("------------------# 2 keyword argument------------------------")
get_power(action="myaction", type="mytype", voltage=1000)  # 2 keyword argument
print("------------------------------------------")
get_power(voltage=1000000, action='VOOOOOM')               # 2 keyword arguments
print("------------------------------------------")
get_power(action='VOOOOOM', voltage=1000000)               # 2 keyword arguments
print("------------------------------------------")
print("------------------------------------------")
get_power(1000, action='Hello World')           # 1 positional, 1 keyword
print("------------------------------------------")



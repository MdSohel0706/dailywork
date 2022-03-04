'''
1. Builtin packages,modules             # python software directory Lib*
   C:\Users\madhu\AppData\Local\Programs\Python\Python36\Lib

2. User defined packages,modules       # with in python project*
   With in project directory

3. External defined packages,modules    # python -m pip install <lib_name>  (site-packages)*
   C:\Users\madhu\AppData\Local\Programs\Python\Python36\Lib\site-packages

'''

"""Functions


-->Functions are basically some instructions that are packaged to.gether to perform a specific task. To create a fucntion we use the "def" keyword. 

example:
----------
def func() :
	pass
print(func()) #this calls the function, but it returns none becuase there nothing in the function.
print(func) #this prints the function with particular location.
print(id(func)) #this return the id of the func.

Note: the id and the memory location are different. id is an integer value and the memory location is the alpha numeric value.

-->We can also use the methods like upper and lower on the functions.
example:
def func():
	return "hello world"
print(func().upper()) #the result will be printed in the upper case
pirnt(func().lower())

-->to pass many number of the arguments to the function we have to keep on create the new variables. to avoid that we use the positional and the keyword arguments. The positional argument takes the values as the tuple and the keyword argument takes the values as the key value pairs, simply dictionary values. 
example:
--------
def func(*args, **kwargs):
    print(args)
    print(kwargs)

func('math', 'args', name = 'venkat', age = 26)

-->We can also pass the tuples and the dict as the argument to the function. But it takes the all as the tuple. So unpack these values we use the same notation, like we have to keep * and **.
example:
--------
def func(*args, **kwargs):
    print(args)
    print(kwargs)

arguments = ['venkat', 'age', ' addres']
keyword_arguments = {'name' :'venkat' , 'age' : 26}
func(*arguments, **keyword_arguments)

-->sample program for finding the days in month and the leap year
example:
--------
months =[31,28, 30, 31,30,31,30,31,30,31,30,31]

def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 !=0):

def days_in_month(year, month):
    if not 1<= month <= 12:
        return 'invalid month'
    if month == 2 and is_leap(year):
        return 29
    return months[month]
print(days_in_month(2000,2))

example:
---------
def is_leap_year(year):

    #check if the year is divisable by 4
    if year % 4 == 0:
        #check if year is divisable by 100        
        if year % 100 == 0:
            #check if year is divisable by 400
            if year % 400 == 0:
                return True
            return False
        return True

print(is_leap_year(96))"""
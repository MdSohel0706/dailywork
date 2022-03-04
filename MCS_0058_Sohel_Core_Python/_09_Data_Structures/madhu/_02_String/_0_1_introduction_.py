
'''
Datatypes
numbers  : int float
boolean  : True False
'''

# STRING  # Group of characters
'''
Registration Form
=====================
EID         : 2343       -- int 
First name  : Madhu      -- String
Last name   : Nettem     -- String
DOB         : XXXXX      -- String
Contact no  : 4312432    -- String
MailID      : fsadsfsdf@gmail.com -- String
Password    : 
'''

str1 = 'Hello World'  # "Hello World"
print(str1)

ch = 'A'  # "A"
print(ch)

ch  = '1'  # "1"
print(ch,type(ch))
print("Addition :", int(ch)+2)

ch = '1.5'
print("Addition : ", float(ch)+2.7)

ch = '*'
print(ch,type(ch))


# Litres ML
# KM M  CM MM
# KG Grams MG
# Litres KM KG  --< Not Possible
print("-----Conversions----------")
x = 10
y = "20"
print(x, y, type(x), type(y))

if type(x) == type(y):
    print("Addition :", x+y)
else:
    print("Addition is not possible")


'''
Data Structures:  
----------------
Set 
Matrix 
Sequence and Series
'''
x = 10
print("------------String for loop------------")
for char in 'Hello World':  # A 65 a 97
    print(char)

print("------------CRUD Operations------------")
# CRUD Operations
x = 10     # CREATE    Write operation
print(x)   # RETRIEVE  Read operation
x = 20     # UPDATE
del x      # DELETE





# Python Variables:
""". A variable is created the moment we first assign a value to it. A
variable is a name given to a memory location. It is the basic unit of storage in a
program.
"""

""" 
1 The value stored in a variable can be changed during program execution.
2. A  variable is only a name given to a memory location, all the operations done on the
variable effects that memory location.
"""
# Rules for creating variables in Python:
"""1.A variable name must start with a letter or the underscore character.
2.A variable name cannot start with a number.
3.A variable name can only contain alpha-numeric characters and underscores (A-z,
0-9, and _ ).
4.Variable names are case-sensitive (name, Name and NAME are three different
variables).
5 The reserved words(keywords) cannot be used naming the variable."""

""""x = 10
For
ex: Binary
values
from decimal number

x = 10: Writing
data
00001010 <-> 1
byte
00001010
"""

"""
PYTHON VARIABLES:?
   A variable is created the moment we first assign a value to it.
   Variable is a name that is used to refer to memory location. Python variable is also known as an identifier and used to hold value.
   A variable is a name given to a memory location. It is the basic unit of storage in a
   program.

   In Python, we don't need to specify the type of variable because Python is a infer language and smart enough to get variable type.
   Variable names can be a group of both the letters and digits, but they have to begin with a letter or an underscore.
   It is recommended to use lowercase letters for the variable name. Rahul and rahul both are two different variables.


----------------------------------------------------------------------------------------------------------------------------------------------------------------

***IDENTIFIER NAMING:?
1.Variables are the example of identifiers. An Identifier is used to identify the literals used in the program. The rules to name an identifier are given below.
2. The first character of the variable must be an alphabet or underscore ( _ ).
3. All the characters except the first character may be an alphabet of lower-case(a-z), upper-case (A-Z), underscore, or digit (0-9).
4. Identifier name must not contain any white-space, or special character (!, @, #, %, ^, &, *).
5. Identifier name must not be similar to any keyword defined in the language.
6. Identifier names are case sensitive; for example, my name, and MyName is not the same.
7. Examples of valid identifiers: a123, _n, n_9, etc.
8. Examples of invalid identifiers: 1a, n%4, n 9, etc.
9.The value stored in a variable can be changed during program execution.
10. A  variable is only a name given to a memory location, all the operations done on the
variable effects that memory location.

---------------------------------------------------------------------------------------------------------------
#Rules for creating variables in Python:
1.A variable name must start with a letter or the underscore character.
2.A variable name cannot start with a number.
3.A variable name can only contain alpha-numeric characters and underscores (A-z,
0-9, and _ ).
4.Variable names are case-sensitive (name, Name and NAME are three different
variables).
5 The reserved words(keywords) cannot be used naming the variable.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DECLARING VARIABLES AND ASSIGNING VALUES:?

1. Python does not bind us to declare a variable before using it in the application. It allows us to create a variable at the required time.
2. We don't need to declare explicitly variable in Python. When we assign any value to the variable, that variable is declared automatically.
3. The equal (=) operator is used to assign value to a variable.

------------------------------------------------------------------------------------------------------------
OBJECT REFERENCES:?

1.It is necessary to understand how the Python interpreter works when we declare a variable. 
2.The process of treating variables is somewhat different from many other programming languages.
3.Python is the highly object-oriented programming language; that's why every data item belongs to a specific type of class. 

Consider the following example.

print("John")  
Output:
John

4.The Python object creates an integer object and displays it to the console. In the above print statement, we have created a string object. Let's check the type of it using the Python built-in type() function.

type("John")  
Output:

<class 'str'>
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

OBJECT IDENTITY:?

1. In Python, every created object identifies uniquely in Python. 
2. Python provides the guaranteed that no two objects will have the same identifier. 
3. The built-in id() function, is used to identify the object identifier.

**Consider the following example.*

a = 50  
b = a  
print(id(a))  
print(id(b))  
# Reassigned variable a  
a = 500  
print(id(a)) 


*Output:*

140734982691168
140734982691168
2822056960944

4.We assigned the b = a, a and b both point to the same object. 
5.When we checked by the id() function it returned the same number. 
6.We reassign a to 500; then it referred to the new object identifier.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
VARIABLE NAMES:?

  We have already discussed how to declare the valid variable. Variable names can be any length can have uppercase, lowercase (A to Z, a to z), the digit (0-9), and underscore character(_). Consider the following example of valid variables names.

*input*
name = "Devansh"  
age = 20  
marks = 80.50  

print(name)  
print(age)  
print(marks)  

*Output:*

Devansh
20
80.5

Consider the following valid variables name.

name = "A"  
Name = "B"  
naMe = "C"  
NAME = "D"  
n_a_m_e = "E"  
_name = "F"  
name_ = "G"  
name = "H"  
na56me = "I"  

print(name,Name,naMe,NAME,n_a_m_e, NAME, n_a_m_e, name, name,_name, na56me)  

*Output:*

A B C D E D E F G F I
----------------------------------------------------------------------------------------------------------------------------------------------------
MULTIWORD KEYWORDS:?

1.Camel Case - In the camel case, each word or abbreviation in the middle of begins with a capital letter. There is no intervention of whitespace.

 For example - nameOfStudent, valueOfVaraible, etc.
2.Pascal Case - It is the same as the Camel Case, but here the first word is also capital. 

For example - NameOfStudent, etc.
3.Snake Case - In the snake case, Words are separated by the underscore. 

For example - name_of_student, etc.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
MULTIPLE ASSIGNMENT:?

1.Python allows us to assign a value to multiple variables in a single statement, which is also known as multiple assignments.

2.We can apply multiple assignments in two ways, either by assigning a single value to multiple variables or assigning multiple values to multiple variables. 

Consider the following example.

1. Assigning single value to multiple variables

Eg:

x=y=z=50    
print(x)    
print(y)    
print(z)    

*Output:*

50  
50  
50  

2. Assigning multiple values to multiple variables:

Eg:

a,b,c=5,10,15    
print a    
print b    
print c    

*Output:*

5  
10  
15  
The values will be assigned in the order in which variables appear.
-----------------------------------------------------------------------------------------------------------------------------------------------
PYTHON VARIABLE TYPES:?

**There are two types of variables in Python - Local variable and Global variable. Let's understand the following variables.

1.LOCAL VARIABLES:

  Local variables are the variables that declared inside the function and have scope within the function. Let's understand the following example.

**Example -

# Declaring a function  
def add():  
    # Defining local variables. They has scope only within a function  
    a = 20  
    b = 30  
    c = a + b  
    print("The sum is:", c)  

# Calling a function  
add()  

*Output:*

The sum is: 50

*Explanation:*

  In the above code, we declared a function named add() and assigned a few variables within the function. 
  These variables will be referred to as the local variables which have scope only inside the function. 
  If we try to use them outside the function, we get a following error.


add()  
# Accessing local variable outside the function   
print(a) 

*Output:*

The sum is: 50
    print(a)
NameError: name 'a' is not defined

We tried to use local variable outside their scope; it threw the NameError.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
GLOBAL VARIABLES:?

    Global variables can be used throughout the program, and its scope is in the entire program.
    We can use global variables inside or outside the function.
    A variable declared outside the function is the global variable by default.
    Python provides the global keyword to use global variable inside the function. 
    If we don't use the global keyword, the function treats it as a local variable. 

Let's understand the following example.

*Example -*

# Declare a variable and initialize it  
x = 101  

# Global variable in function  
def mainFunction():  
    # printing a global variable  
    global x  
    print(x)  
    # modifying a global variable  
    x = 'Welcome To Javatpoint'  
    print(x)  

mainFunction()  
print(x)  

*Output:*

101
Welcome To Javatpoint
Welcome To Javatpoint

*Explanation:*

  In the above code, we declare a global variable x and assign a value to it.
  Next, we defined a function and accessed the declared variable using the global keyword inside the function. 
  Now we can modify its value. Then, we assigned a new string value to the variable x.
  Now, we called the function and proceeded to print x. It printed the as newly assigned value of x.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DELETE A VARIABLE:?

   We can delete the variable using the del keyword. 

The syntax is given below.

Syntax -
del <variable_name>  


In the following example, we create a variable x and assign value to it. We deleted variable x, and print it, we get the error "variable x is not defined". The variable x will no longer use in future.

*Example -*

# Assigning a value to x  
x = 6  
print(x)  
# deleting a variable.   
del x  
print(x)  

*Output:*

6

Traceback (most recent call last):
  File "C:/Users/DEVANSH SHARMA/PycharmProjects/Hello/multiprocessing.py", line 389, in 
    print(x)
NameError: name 'x' is not defined
-----------------------------------------------------------------------------------------------------------------------
MAXIMUM POSSIBLE VALUE OF AN INTEGER IN PYTHON:?

   Unlike the other programming languages, Python doesn't have long int or float data types. It treats all integer values as an int data type. Here, the question arises. What is the maximum possible value can hold by the variable in Python? Consider the following example.

*Example -*

# A Python program to display that we can store  
# large numbers in Python  

a = 10000000000000000000000000000000000000000000  
a = a + 1  
print(type(a))  
print (a)  

*Output:*

<class 'int'>
10000000000000000000000000000000000000000001

-------------------------------------------*-----------------------------------
PRINT SINGLE AND MULTIPLE VARIABLES IN PYTHON:?

     We can print multiple variables within the single print statement. 
     Below are the example of single and multiple printing values.

Example - 1 (Printing Single Variable)

# printing single value   
a = 5  
print(a)  
print((a))  

*Output:*

5
5

**Example - 2 (Printing Multiple Variables)

a = 5  
b = 6  
# printing multiple variables  
print(a,b)  
# separate the variables by the comma  
Print(1, 2, 3, 4, 5, 6, 7, 8)   

*Output:*

5 6
1 2 3 4 5 6 7 8

--------------------------------------------------------------------------------------------------------------------------"""

"""x = 10
For
ex: Binary
values
from decimal number

x = 10: Writing
data
00001010 <-> 1
byte
00001010
"""
"""
PYTHON VARIABLES:?
   A variable is created the moment we first assign a value to it.
   Variable is a name that is used to refer to memory location. Python variable is also known as an identifier and used to hold value.
   A variable is a name given to a memory location. It is the basic unit of storage in a
   program.

   In Python, we don't need to specify the type of variable because Python is a infer language and smart enough to get variable type.
   Variable names can be a group of both the letters and digits, but they have to begin with a letter or an underscore.
   It is recommended to use lowercase letters for the variable name. Rahul and rahul both are two different variables.
"""


"""
***IDENTIFIER NAMING:?
1.Variables are the example of identifiers. An Identifier is used to identify the literals used in the program. The rules to name an identifier are given below.
2. The first character of the variable must be an alphabet or underscore ( _ ).
3. All the characters except the first character may be an alphabet of lower-case(a-z), upper-case (A-Z), underscore, or digit (0-9).
4. Identifier name must not contain any white-space, or special character (!, @, #, %, ^, &, *).
5. Identifier name must not be similar to any keyword defined in the language.
6. Identifier names are case sensitive; for example, my name, and MyName is not the same.
7. Examples of valid identifiers: a123, _n, n_9, etc.
8. Examples of invalid identifiers: 1a, n%4, n 9, etc.
9.The value stored in a variable can be changed during program execution.
10. A  variable is only a name given to a memory location, all the operations done on the
variable effects that memory location.
---------------------------------------------------------------------------------------------------------------
***Rules for creating variables in Python:
1.A variable name must start with a letter or the underscore character.
2.A variable name cannot start with a number.
3.A variable name can only contain alpha-numeric characters and underscores (A-z,
0-9, and _ ).
4.Variable names are case-sensitive (name, Name and NAME are three different
variables).
5 The reserved words(keywords) cannot be used naming the variable.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DECLARING VARIABLES AND ASSIGNING VALUES:?

1. Python does not bind us to declare a variable before using it in the application. It allows us to create a variable at the required time.
2. We don't need to declare explicitly variable in Python. When we assign any value to the variable, that variable is declared automatically.
3. The equal (=) operator is used to assign value to a variable.

------------------------------------------------------------------------------------------------------------
OBJECT REFERENCES:?

1.It is necessary to understand how the Python interpreter works when we declare a variable. 
2.The process of treating variables is somewhat different from many other programming languages.
3.Python is the highly object-oriented programming language; that's why every data item belongs to a specific type of class. 

Consider the following example.

print("John")  
Output:
John

4.The Python object creates an integer object and displays it to the console. In the above print statement, we have created a string object. Let's check the type of it using the Python built-in type() function.

type("John")  
Output:

<class 'str'>
-------------------------------------------------------------------------------------------------------------------------------------------------

OBJECT IDENTITY:?

1. In Python, every created object identifies uniquely in Python. 
2. Python provides the guaranteed that no two objects will have the same identifier. 
3. The built-in id() function, is used to identify the object identifier.

**Consider the following example.*

a = 50  
b = a  
print(id(a))  
print(id(b))  
# Reassigned variable a  
a = 500  
print(id(a)) 


*Output:*

140734982691168
140734982691168
2822056960944

4.We assigned the b = a, a and b both point to the same object. 
5.When we checked by the id() function it returned the same number. 
6.We reassign a to 500; then it referred to the new object identifier.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
VARIABLE NAMES:?

  We have already discussed how to declare the valid variable. Variable names can be any length can have uppercase, lowercase (A to Z, a to z), the digit (0-9), and underscore character(_). Consider the following example of valid variables names.

*input*
name = "Devansh"  
age = 20  
marks = 80.50  

print(name)  
print(age)  
print(marks)  

*Output:*

Devansh
20
80.5

Consider the following valid variables name.

name = "A"  
Name = "B"  
naMe = "C"  
NAME = "D"  
n_a_m_e = "E"  
_name = "F"  
name_ = "G"  
name = "H"  
na56me = "I"  

print(name,Name,naMe,NAME,n_a_m_e, NAME, n_a_m_e, name, name,_name, na56me)  

*Output:*

A B C D E D E F G F I
----------------------------------------------------------------------------------------------------------------------------------------------------
MULTIWORD KEYWORDS:?

1.Camel Case - In the camel case, each word or abbreviation in the middle of begins with a capital letter. There is no intervention of whitespace.

 For example - nameOfStudent, valueOfVaraible, etc.
2.Pascal Case - It is the same as the Camel Case, but here the first word is also capital. 

For example - NameOfStudent, etc.
3.Snake Case - In the snake case, Words are separated by the underscore. 

For example - name_of_student, etc.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
MULTIPLE ASSIGNMENT:?

1.Python allows us to assign a value to multiple variables in a single statement, which is also known as multiple assignments.

2.We can apply multiple assignments in two ways, either by assigning a single value to multiple variables or assigning multiple values to multiple variables. 

Consider the following example.

1. Assigning single value to multiple variables

Eg:

x=y=z=50    
print(x)    
print(y)    
print(z)    

*Output:*

50  
50  
50  

2. Assigning multiple values to multiple variables:

Eg:

a,b,c=5,10,15    
print a    
print b    
print c    

*Output:*

5  
10  
15  
The values will be assigned in the order in which variables appear.
-----------------------------------------------------------------------------------------------------------------------------------------------
PYTHON VARIABLE TYPES:?

**There are two types of variables in Python - Local variable and Global variable. Let's understand the following variables.

1.LOCAL VARIABLES:

  Local variables are the variables that declared inside the function and have scope within the function. Let's understand the following example.

**Example -

# Declaring a function  
def add():  
    # Defining local variables. They has scope only within a function  
    a = 20  
    b = 30  
    c = a + b  
    print("The sum is:", c)  

# Calling a function  
add()  

*Output:*

The sum is: 50

*Explanation:*

  In the above code, we declared a function named add() and assigned a few variables within the function. 
  These variables will be referred to as the local variables which have scope only inside the function. 
  If we try to use them outside the function, we get a following error.


add()  
# Accessing local variable outside the function   
print(a) 

*Output:*

The sum is: 50
    print(a)
NameError: name 'a' is not defined

We tried to use local variable outside their scope; it threw the NameError.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
GLOBAL VARIABLES:?

    Global variables can be used throughout the program, and its scope is in the entire program.
    We can use global variables inside or outside the function.
    A variable declared outside the function is the global variable by default.
    Python provides the global keyword to use global variable inside the function. 
    If we don't use the global keyword, the function treats it as a local variable. 

Let's understand the following example.

*Example -*

# Declare a variable and initialize it  
x = 101  

# Global variable in function  
def mainFunction():  
    # printing a global variable  
    global x  
    print(x)  
    # modifying a global variable  
    x = 'Welcome To Javatpoint'  
    print(x)  

mainFunction()  
print(x)  

*Output:*

101
Welcome To Javatpoint
Welcome To Javatpoint

*Explanation:*

  In the above code, we declare a global variable x and assign a value to it.
  Next, we defined a function and accessed the declared variable using the global keyword inside the function. 
  Now we can modify its value. Then, we assigned a new string value to the variable x.
  Now, we called the function and proceeded to print x. It printed the as newly assigned value of x.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DELETE A VARIABLE:?

   We can delete the variable using the del keyword. 

The syntax is given below.

Syntax -
del <variable_name>  


In the following example, we create a variable x and assign value to it. We deleted variable x, and print it, we get the error "variable x is not defined". The variable x will no longer use in future.

*Example -*

# Assigning a value to x  
x = 6  
print(x)  
# deleting a variable.   
del x  
print(x)  

*Output:*

6

Traceback (most recent call last):
  File "C:/Users/DEVANSH SHARMA/PycharmProjects/Hello/multiprocessing.py", line 389, in 
    print(x)
NameError: name 'x' is not defined
-----------------------------------------------------------------------------------------------------------------------
MAXIMUM POSSIBLE VALUE OF AN INTEGER IN PYTHON:?

   Unlike the other programming languages, Python doesn't have long int or float data types. It treats all integer values as an int data type. Here, the question arises. What is the maximum possible value can hold by the variable in Python? Consider the following example.

*Example -*

# A Python program to display that we can store  
# large numbers in Python  

a = 10000000000000000000000000000000000000000000  
a = a + 1  
print(type(a))  
print (a)  

*Output:*

<class 'int'>
10000000000000000000000000000000000000000001

-------------------------------------------*-----------------------------------
PRINT SINGLE AND MULTIPLE VARIABLES IN PYTHON:?

     We can print multiple variables within the single print statement. 
     Below are the example of single and multiple printing values.

**Example - 1 (Printing Single Variable)

# printing single value   
a = 5  
print(a)  
print((a))  

*Output:*

5
5

**Example - 2 (Printing Multiple Variables)

a = 5  
b = 6  
# printing multiple variables  
print(a,b)  
# separate the variables by the comma  
Print(1, 2, 3, 4, 5, 6, 7, 8)   

*Output:*

5 6
1 2 3 4 5 6 7 8

--------------------------------------------------------------------------------------------------------------------------

x = 10
For
ex: Binary
values
from decimal number

x = 10: Writing
data
00001010 <-> 1
byte
00001010


--------------------------------------------------**--------------------------------------------------"""

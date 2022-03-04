
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

'''str1 = 'Hello World'  # "Hello World"
print(str1)'''

'''ch = 'A'  # "A"
print(ch)'''

ch  = '1'  # "1"
'''print(ch,type(ch))
print("Addition :", int(ch)+2)'''

'''ch = '1.5'
print("Addition : ", float(ch)+2.7)'''

'''ch = '*'
print(ch,type(ch))'''


# Litres ML
# KM M  CM MM
# KG Grams MG
# Litres KM KG  --< Not Possible
'''print("-----Conversions----------")
x = 10
y = "20"
print(x, y, type(x), type(y))

if type(x) == type(y):
    print("Addition :", x+y)
else:
    print("Addition is not possible")'''


'''
Data Structures:  
----------------
Set 
Matrix 
Sequence and Series
'''
'''x = 10
print("------------String for loop------------")
for char in 'Hello World':  # A 65 a 97
    print(char)

print("------------CRUD Operations------------")
# CRUD Operations
x = 10     # CREATE    Write operation
print(x)   # RETRIEVE  Read operation
x = 20     # UPDATE
del x      # DELETE'''


'''name = "satish"
print(name)

ch = "a"
print(ch, type(ch))'''

'''ch = 23
print("Addition of two numbers: ",ch,ch+53,type(ch))'''

'''float = 43.87
print("Addition of Numbers :", float+43.56,type(float))'''

'''ch = "*"
print(ch,type(ch))'''

'''x = 10
y = "34"
print(x,y,type(x),type(y))'''


"""**STRING:
1.String is a collection of alphabets, words or other characters.
2.It is one of the primitive data structures and are the building blocks for data manipulation.
3.Python has a built-in string class named str .
4.Python strings are "immutable" which means they cannot be changed after they are created
5.Strings in Python can be created using single quotes or double quotes or even triple quotes.

"""
"""*Python string is the collection of the characters surrounded by single quotes, double quotes, or triple quotes.
The computer does not understand the characters; internally, it stores manipulated character as the combination of the 0's and 1's.

*Each character is encoded in the ASCII or Unicode character.
So we can say that Python strings are also called the collection of Unicode characters.

*In Python, strings can be created by enclosing the character or the sequence of characters in the quotes.
Python allows us to use single quotes, double quotes, or triple quotes to create the string.

**CREATING STRING IN PYTHON:

1.We can create a string by enclosing the characters in single-quotes or double- quotes.
2.Python also provides triple-quotes to represent the string
but it is generally used for multiline string or docstrings.
-------------------------------*-----------------------------------------------

** STRINGS INDEXING AND SPLITTING:

1.Like other languages, the indexing of the Python strings starts from 0
2.the slice operator [] is used to access the individual characters of the string.
However, we can use the : (colon) operator in Python to access the substring from the given string.
3.upper range given in the slice operator is always exclusive i.e.
if str = 'HELLO' is given, then str[1:3] will always include str[1] = 'E', str[2] = 'L'
4.We can do the negative slicing in the string
it starts from the rightmost character, which is indicated as -1. The second rightmost index indicates -2
------------------------------**------------------------------------------
* DELETING /UPDATING FROM A STRING:

1.In Python, Updation or deletion of characters from a String is not allowed.
2.This will cause an error because item assignment or item deletion from a String is not supported.
3.Although deletion of entire String is possible with the use of a built-in del keyword.
4.This is because Strings are immutable, hence elements of a String cannot be changed once it has been assigned.
Only new strings can be reassigned to the same name.



***Deleting Entire String:

Deletion of entire string is possible with the use of del keyword.
 Further, if we try to print the string, this will produce an error because String is deleted and is unavailable to be printed.

'''
'''***ESCAPE SEQUENCING IN PYTHON:?

1.While printing Strings with single and double quotes in it causes SyntaxError 
because String already contains Single and Double Quotes and hence cannot be printed with the use of either of these. 
Hence, to print such a String either Triple Quotes are used or Escape sequences are used to print such Strings. 

2.Escape sequences start with a backslash and can be interpreted differently.
If single quotes are used to represent a string, then all the single quotes present in the string must be escaped and same is done for Double Quotes. 


To ignore the escape sequences in a String, r or R is used, this implies that the string is a raw string and escape sequences inside it are to be ignored.



-------------------------------------------------------**--------------------------------------------------
'''
'''FORMATING OF STRINGS:?

1.Strings in Python can be formatted with the use of format() method which is very versatile and powerful tool for formatting of Strings.
Format method in String contains curly braces {} as placeholders which can hold arguments according to position or keyword to specify the order.


----------------**---------------------------------------------------------------------------------------------
'''
'''** STRING OPERATORS:?

OPERATOR                           DESCRIPTION


+	                    It is known as concatenation operator used to join the strings given either side of the operator.

*	                    It is known as repetition operator. 
                        It concatenates the multiple copies of the same string.

[]	                    It is known as slice operator. 
                        It is used to access the sub-strings of a particular string.

[:]	                    It is known as range slice operator. 
                        It is used to access the characters from the specified range.

in	                    It is known as membership operator. 
                        It returns if a particular sub-string is present in the specified string.

not in	                It is also a membership operator and does the exact reverse of in. 
                        It returns true if a particular substring is not present in the specified string.

r/R	                    It is used to specify the raw string. 
                        Raw strings are used in the cases where we need to print the actual meaning of escape characters such as "C://python". 
                        To define any string as a raw string, the character r or R is followed by the string.

%	                    It is used to perform string formatting. 
                        It makes use of the format specifiers used in C programming like %d or %f to map their values in python. We will discuss how formatting is done in python.


------------------------------------------*--------------------------------------------------------------------

**PYTHON STRING FORMATTING:

1.Escape Sequence:

 text as - They said, "Hello what's going on?"- the given statement can be written in single quotes or double quotes but it will raise the SyntaxError as it contains both single and double-quotes.

*Example*

str = "They said, "Hello what's going on?""  
print(str) 

*Output:*

SyntaxError: invalid syntax


We can use the triple quotes to accomplish this problem but Python provides the escape sequence.

The backslash(/) symbol denotes the escape sequence. 
The backslash can be followed by a special character and it interpreted differently. 
The single quotes inside the string must be escaped. We can apply the same as in the double quotes.

------------------------------------------------*---------------------------------------------------------------------


**LIST OF ESCAPE SEQUENCES:?


1.	\newline	                       

It ignores the new line.	

EXAMPLE:

print("Python1 \
Python2 \
Python3")

*Output:*
Python1 Python2 Python3
--------**------------

2.	\\	Backslash

print("\\")

*Output:*
\
---------------*----------------

3.	\'	Single Quotes

print('\'')

*Output:*
'

------------*-----------------

4.	\\''	Double Quotes	

print("\"")

*Output:*
"

------------------*--------

4.	\\''	Double Quotes	

print("\"")

*Output:*
"
------------*---------

5.	\a	ASCII Bell	

print("\a")

--------------**-------------

6.	\b	ASCII Backspace(BS)	

print("Hello \b World")

*Output:*
Hello World

-----------------*--------------

7.	\f	ASCII Formfeed	

print("Hello \f World!")

Hello  World!

-------------*----------------

8.	\n	ASCII Linefeed	

print("Hello \n World!")

*Output:*
Hello
 World!

 --------------------*--------------

9.	\r	ASCII Carriege Return(CR)	

print("Hello \r World!")

*Output:*
World!

-------------------*-----------------

10.	\t	ASCII Horizontal Tab	

print("Hello \t World!")

*Output:*
Hello 	 World!

---------------*-------------

11.	\v	ASCII Vertical Tab	

print("Hello \v World!")

**Output:*
Hello 
 World!

 -----------------*------------

12.	\ooo	Character with octal value	

print("\110\145\154\154\157")

*Output:*
Hello

-------------*---------------

13	\xHH	Character with hex value.	

print("\x48\x65\x6c\x6c\x6f")

*Output:*
Hello


---------------------------------------------------------*****------------------------------------------------------------

*THE FORMAT() METHOD:*

1.The format() method is the most flexible and useful method in formatting strings. 
2.The curly braces {} are used as the placeholder in the string and replaced by the format() method argument.

*EXAMPLE*
# Using Curly braces  
print("{} and {} both are the best friend".format("Devansh","Abhishek"))  

#Positional Argument  
print("{1} and {0} best players ".format("Virat","Rohit"))  

#Keyword Argument  
print("{a},{b},{c}".format(a = "James", b = "Peter", c = "Ricky"))  


*Output:*

Devansh and Abhishek both are the best friend
Rohit and Virat best players 
James,Peter,Ricky 

--------------------------------------*------------------------------------------------------------------

*PYTHON STRING FORMATTING USING % OPERATOR:*

    Python allows us to use the format specifiers used in C's printf statement. 
    The format specifiers in Python are treated in the same way as they are treated in C. 
    However, Python provides an additional operator %, which is used as an interface between the format specifiers and their values. 
    In other words, we can say that it binds the format specifiers to the values.

* example.*

Integer = 10;    
Float = 1.290    
String = "Devansh"    
print("Hi I am Integer ... My value is %d\nHi I am float ... My value is %f\nHi I am string ... My value is %s"%(Integer,Float,String))    

*Output:*

Hi I am Integer ... My value is 10
Hi I am float ... My value is 1.290000
Hi I am string ... My value is Devansh

----------------------------------------------------**---------------------------------------------------------

**STRING FORMATING OPERATORS:

Format Symbol	                            Conversion

%c	                                       character
%s	                                       string conversion via str() prior to formatting
%i	                                       signed decimal integer
%d	                                       signed decimal integer
%u	                                       unsigned decimal integer
%o	                                       octal integer
%x	                                       hexadecimal integer (lowercase letters)
%X	                                       hexadecimal integer (UPPERcase letters)
%e	                                       exponential notation (with lowercase 'e')
%E	                                       exponential notation (with UPPERcase 'E')
%f	                                       floating point real number
%g	                                       the shorter of %f and %e
%G	                                       the shorter of %f and %E


----------------------------------------**-----------------------------------------------------------------------------

**STRING CONCATINATION:

String Concatenation is the technique of combining two strings. 
String Concatenation can be done using many ways.
We can perform string concatenation using following ways:


1.Using + operator 

2.Using join() method 

3.Using % operator 

4.Using format() function 

5.Using , (comma)"""





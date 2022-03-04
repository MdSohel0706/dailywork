#state : Does not change
#behavior : To perform specific actions


#EXAMPLE PROGRAMS:

#METHOD 1 CAPITALIZE()

"""str1 = "Well come to home"
print("Enter the String : ",str1.capitalize())"""
#----------------------------------------------------------------------------------------------------------------------
"""list_1 = [1,2,3,"MCS",4,"Software",5,"Python",6]
digits = []
chars = []
for i in list_1:
    if type(i) == int:
        digits.append(i)
    elif type(i) == str:
        chars.append(i)
list_2 = chars+digits
print(list_2)

# output
#['MCS', 'Software', 'Python', 1, 2, 3, 4, 5, 6]"""
#---------------------------------------------------------------------------------------------------------------
"""list_1 = [1,2,3,"MCS",4,"Software",5,"Python",6]
digits = []
chars = []
for i in list_1:
    if str(i).isdigit():
        digits.append(i)
    elif i.isalpha():
        chars.append(i)
list_2 = chars+digits
print(list_2)

 # ['MCS', 'Software', 'Python', 1, 2, 3, 4, 5, 6]"""

#----------------------------------------------------------------------------------------------------------------------------

"""list_1 = [1,2,3,"MCS",4,"Software",5,"Python",6]
digits = []
chars = []
for i in list_1:
    if isinstance[i,int]:
        digits.append(i)
    elif isinstance[i,chars]:
        chars.append(i)
list_2 = chars+digits
print(list_2)
"""

#-----------------------------------------------------------------------------------------------------------------
str1 = "abc"
str2 = "defg"
result = []
for i,j in zip(str1,str2):
    result.append(i)
    result.append(j)
result.append(str2[-1])
print(result)

#output: join : ['a', 'd', 'b', 'e', 'c', 'f', 'g']

#--------------------------------------------------------------------------------------------------------------------------
chars = "karnataka"
check_string = "how many times each character repeating"

for char in chars:
    count = check_string.count(char)
if (count > 1):
   print(char,count)

#--------------------------------------------------------------------------------------------------------------------
"""
STRING PROGRAMS:

1.Write a Python Program to Replace all Occurrences of ‘a’ with $ in a String?

string=input("Enter string:")
string=string.replace('a','$')
string=string.replace('A','$')
print("Modified string:")
print(string)

2.Write a Python Program to Detect if Two Strings are Anagrams?
s1=raw_input("Enter first string:")
s2=raw_input("Enter second string:")
if(sorted(s1)==sorted(s2)):
      print("The strings are anagrams.")
else:
      print("The strings aren't anagrams.")
3.Python Program to Form a New String where the First Character and the Last Character have been Exchanged?

def change(string):
      return string[-1:] + string[1:-1] + string[:1]
string=raw_input("Enter string:")
print("Modified string:")
print(change(string))

4.Python Program to Count the Number of Vowels in a String?

string=raw_input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)

5.Python Program to Take in a String and Replace Every Blank Space with Hyphen.?

string=raw_input("Enter string:")
string=string.replace(' ','-')
print("Modified string:")
print(string)

6.Python Program to Calculate the Length of a String Without Using a Library Function?

string=raw_input("Enter string:")
count=0
for i in string:
      count=count+1
print("Length of the string is:")
print(count)

7.Python Program to Remove the Characters of Odd Index Values in a String?

def modify(string):
  final = ""
  for i in range(len(string)):
    if i % 2 == 0:
      final = final + string[i]
  return final
string=raw_input("Enter string:")
print("Modified string is:")
print(modify(string))

8.Python Program to Calculate the Number of Words and the Number of Characters Present in a String?

string=raw_input("Enter string:")
char=0
word=1
for i in string:
      char=char+1
      if(i==' '):
            word=word+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)

9.Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions?

string1=raw_input("Enter first string:")
string2=raw_input("Enter second string:")
count1=0
count2=0
for i in string1:
      count1=count1+1
for j in string2:
      count2=count2+1
if(count1<count2):
      print("Larger string is:")
      print(string2)
elif(count1==count2):
      print("Both strings are equal.")
else:
      print("Larger string is:")
      print(string1)

10.Python Program to Count Number of Lowercase Characters in a String?

string=raw_input("Enter string:")
count=0
for i in string:
      if(i.islower()):
            count=count+1
print("The number of lowercase characters is:")
print(count)

11.Python Program to Check if a String is a Palindrome or Not?

string=raw_input("Enter string:")
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")

12.Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String?

string=raw_input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)

13.Python Program to Accept a Hyphen Separated Sequence of Words as Input
and Print the Words in a Hyphen-Separated Sequence after Sorting them Alphabetically

Problem Solution
1. Take a hyphen separated sequence of words from the user.
2. Split the words in the input with hyphen as reference and store the words in a list.
3. Sort the words in the list.
4. Join the words in the list with hyphen between them and print the sorted sequence.
5. Exit.

Program:

print("Enter a hyphen separated sequence of words:")
lst=[n for n in raw_input().split('-')]
lst.sort()
print("Sorted:")
print('-'.join(lst))

14.Python Program to Calculate the Number of Digits and Letters in a String?

string=raw_input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.isdigit()):
            count1=count1+1
      count2=count2+1
print("The number of digits is:")
print(count1)
print("The number of characters is:")
print(count2)

15.Python Program to Form a New String Made of the First 2 and Last 2 characters From a Given String?

string=raw_input("Enter string:")
count=0
for i in string:
      count=count+1
new=string[0:2]+string[count-2:count]
print("Newly formed string is:")
print(new)

16.Python Program to Count the Occurrences of Each Word in a Given String Sentence?

string=raw_input("Enter string:")
word=raw_input("Enter word:")
a=[]
count=0
a=string.split(" ")
for i in range(0,len(a)):
      if(word==a[i]):
            count=count+1
print("Count of the word is:")
print(count)

17.Python Program to Check if a Substring is Present in a Given String?

string=raw_input("Enter string:")
sub_str=raw_input("Enter word:")
if(string.find(sub_str)==-1):
      print("Substring not found in string!")
else:
      print("Substring in string!")

18.Python Program to Check Whether a String is a Palindrome or not Using Recursion?

def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=str(input("Enter string:"))
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")

19.write a program to store all the vowels from the given string by using while loop?

st="suma"
res=''
i=0
whilei<len(s):
     if s[i] in "aeiouAEIOU":
           res+=st[i]
     i+=1
print(res)

20. write a program to check whether the given string is palindrome or not whithout using slicing?

string="madam"
res=" "
i=0
while i<len(string):
      res=string[i]+res
i+=1
if res==string:
   print("the given string is palindrome")
else:
   print("the given string is not palindrome")

21.wap to check whether the given number is palindrome or not without using type casting as well as slicing?

num=143
rev=0
temp=num
while temp!=0:
      ld=temp%10
      temp=temp//10
      rev=rev*10+ld
if num==rev:
      print("the given num is palindrome")
else:
     print("the given num is not plindrome")

22. wap to convert all the lowercase characters into uppercase characters present iside a given string?

st="suma priya"
res=" "
for i in st:
      if "a"<=i<="z":
          res=res+chr(ord(i)-32)
      else:
         res+=i
print(res)

23.wap to store &print all the uppercase characters ,lowercase character,numeric values and special characters from the given string separately?


s="sUma@$123"
upper=""
lower=""
special=""
num=""
for i in s:
     if "A'<=i<="Z":
         upper+=1
     elif 'a'<=i<='z':
         lower+=1
     elif '0'<=i<='9':
         num+=1
     else:
        special+=1
print(upper,lower,special,num)
print(upper)
print(lower)
print(special)
print(num)

24. wap to split the given string into no of pieces when the specified character is found?

s="hello good morning"
res=[""]
ch='o'
for i in s:
    if i==ch:
       res.append('')
    else:
       res[-1]+=i
print(res)

25.wap to split the given string into no of pieces when the specified character is found and that is for specified number of times?

s="hello good morning"
res=[""]
ch='o'
n=4
for i in s:
    if i==ch and len(res)<=n:
       res.append('')
    else:
       res[-1]+=i
print(res)


26.Python Program to Update character of a String?

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Updating a character
# of the String
String1[2] = 'p'
print("\nUpdating character at 2nd Index: ")
print(String1)
 ERROR:
Traceback (most recent call last):
File “/home/360bb1830c83a918fc78aa8979195653.py”, line 10, in
String1[2] = ‘p’
TypeError: ‘str’ object does not support item assignment

27. Python Program to Update entire String?

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Updating a String
String1 = "Welcome to the Geek World"
print("\nUpdated String: ")
print(String1)

28. Python Program to Delete characters from a String?

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Deleting a character
# of the String
del String1[2]
print("\nDeleting character at 2nd Index: ")
print(String1)


Error:

Traceback (most recent call last):
File “/home/499e96a61e19944e7e45b7a6e1276742.py”, line 10, in
del String1[2]
TypeError: ‘str’ object doesn’t support item deletion

29.  Python Program to Delete entire String ?

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Deleting a String
# with the use of del
del String1
print("\nDeleting entire String: ")
print(String1)

Error:

Traceback (most recent call last):
File “/home/e4b8f2170f140da99d2fe57d9d8c6a94.py”, line 12, in
print(String1)
NameError: name ‘String1’ is not defined

30. Python Program for Escape Sequencing of String?

# Initial String
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes: ")
print(String1)

# Escaping Single Quote
String1 = 'I\'m a "Geek"'
print("\nEscaping Single Quote: ")
print(String1)

# Escaping Double Quotes
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ")
print(String1)

# Printing Paths with the
# use of Escape Sequences
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ")
print(String1)

#Output:

Initial String with use of Triple Quotes:
I'm a "Geek"

Escaping Single Quote:
I'm a "Geek"

Escaping Double Quotes:
I'm a "Geek"

Escaping Backslashes:
C:\Python\Geeks\

31.  Printing Geeks in HEX ?
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ")
print(String1)

# Using raw String to
# ignore Escape Sequences
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ")
print(String1)


#Output:

Printing in HEX with the use of Escape Sequences:
This is Geeks in HEX

Printing Raw String in HEX Format:
This is \x47\x65\x65\x6b\x73 in \x48\x45\x58


32.  Python Program for Formatting of Strings?

# Default order
String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print String in default order: ")
print(String1)

# Positional Formatting
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String1 = "{l} {f} {g}".format(g = 'Geeks', f = 'For', l = 'Life')
print("\nPrint String in order of Keywords: ")
print(String1)


#Output:

Print String in default order:
Geeks For Life

Print String in Positional order:
For Geeks Life

33. Formatting of Integers?
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)

# Formatting of Floats
String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

# Rounding off Integers
String1 = "{0:.2f}".format(1/6)
print("\none-sixth is : ")
print(String1)


**Output:

Binary representation of 16 is
10000

Exponent representation of 165.6458 is
1.656458e+02

one-sixth is :
0.17

34.  wap to concatinate  two strings?
y = "awesome"
z =  x + y
print(z)

##OUTPUT
python is awesome


"""
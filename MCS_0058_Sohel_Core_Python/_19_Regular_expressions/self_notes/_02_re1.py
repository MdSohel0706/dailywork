'''
Sequence characters
-------------------
\d : digits (0 - 9)
\D : non digits
\s : white space (\t,\n\,\r,\f,\v)
\S : non white space
\w : represents alphanumeric (A-Z)
\W : represents non - alphanumeric
\b : represents space around words
\A : matches only at start of string
\Z : matches only at end of string

Examples of regular expressions
-------------------------------
r'\W+' - one or more non alphanumeric characters
r'[\W]*' - 0 or more non alphanumeric characters
r'\ba[\w]*\b' - words beginning with a
r'\b\d[\w]*\b' - words beginning with digits
r'\b\w{5}\b' - words having exact length of 5
r'\b\w{4,}\b' - words having length minimum of 4
r'\b\w{3,5}\b' - words having length 3, 4 or 5
r'\b\d\b' - words havings single digits
r'\b\t[\w]*\Z' - to check if the last word of a string starts with t
r'[\d]+' - words having one or more occurrences of digits(eg. phone number)
r'[\D]+' - words having one or more occurrences of non digits
r'a[nk][\w]*' - all words starting with 'an' or 'ak'
r'\d{1,2}-\d{1,2}-\d{4}' - date format dd-mm-yyyy or d-m-yyyy
r'[a-z]' - lower case characters from a to z
r'[A-Z]' - upper case characters from A to Z
r'[A-Z][a-z]*' - words starting with upper case letter and having any length
r'\d[ap]m' or r'\dam|\dpm' - words like '8am', '4pm', etc

Quantifiers
-----------
+ = 1 or more repetitions
* = 0 or more repetitions
? = 0 or 1 repetitions
{m} = exact m occurrences
{m,n} = minimum m and maximum n occurrences, m defaults to 0, n defaults to infinity

Special characters
------------------
\ - escape special characters nature
. - matches any character except new line
^ - matches beginning of a string, eg. r'^He' matches strings like "Hello World" since it starts with 'He'
$ - matches ending of a string, eg. r'World$' matches string like "Hello World" since it ends with 'World' 
[...] - denotes a set of possible characters, eg. [6b-d] - matches '6', 'b', 'c', 'd'
[^...] - matches every character except the ones inside brackets,
eg. [^a-c6] - matches every character except 'a', 'b', 'c', '6'
(...) - matches the regular expression inside the parantheses and the result can be captures
R|S - matches either regex R or regex S


Methods
-------
result = re.search('expression','string') - finds first occurrence of given regular expression in a string
result.group() - extract the string found

result = re.findall('expression','string') - returns list of all matching regular expression in the string

result = re.match('expression','string') - returns matching regular expression 
if it is found at the beginning of the string

result = re.split('expression','string') - splits the string into pieces according to the regular expression
and returns a list of strings

result = re.sub('regular expression', new string, string)

result = re.search(r'world$', str, re.IGNORECASE) - searches if string ends with the given regular expression
ignoring the case 



'''
import re

reg1 = r'm\w\w'
prog1 = re.compile(reg1)
str1 = "cat mat bat rat gemat"
result = prog1.search(str1)
if result:
    print(result.group())

#Another way of doing this
rex = r'm\w{2}'
str = "cat mat bat rat gemat"
result = re.search(rex,str)
print(result.group())

#finding all words starting with 'm' or 'c' and having length of 3
rex = r'm\w{2}|c\w{2}'
str = "cat mat bat rat gemat"
result = re.findall(rex,str)
print(result)

#replace all words starting with 'f' or 'F' with new_word
rex = r'[Ff][\w]*'
str = "France is not a fear filled fool"
result = re.sub(rex, "new_word", str)
print(result)

rex = r'[Ff]'
str = "France is not a fear filled fool"
result = re.split(rex, str)
print(result)





"""

1.capitalize():
   It capitalizes the first character of the String. This function is deprecated in python3

2.casefold():
	It returns a version of s suitable for case-less comparisons

3.center(width ,fillchar):
	It returns a space padded string with the original string centred with equal number of left and right spaces.

4.count(string,begin,end):
	It counts the number of occurrences of a substring in a String between begin and end index.

5.decode(encoding = 'UTF8', errors = 'strict'):
	Decodes the string using codec registered for encoding.

6.encode():
	Encode S using the codec registered for encoding. Default encoding is 'utf-8'.

7.endswith(suffix ,begin=0,end=len(string)):
	It returns a Boolean value if the string terminates with given suffix between begin and end

8.expandtabs(tabsize = 8):
	It defines tabs in string to multiple spaces. The default space value is 8.

9.find(substring ,beginIndex, endIndex):
	It returns the index value of the string where substring is found between begin index and end index.

10.format(value):
	It returns a formatted version of S, using the passed value.

11.index(subsring, beginIndex, endIndex):
	It throws an exception if string is not found. It works same as find() method.

12.isalnum():
	It returns true if the characters in the string are alphanumeric i.e., alphabets or numbers and there is at least 1 character. Otherwise, it returns false.

13.isalpha():
	It returns true if all the characters are alphabets and there is at least one character, otherwise False.

14.isdecimal():
	It returns true if all the characters of the string are decimals.

15.isdigit():
	It returns true if all the characters are digits and there is at least one character, otherwise False.

16.isidentifier():
	It returns true if the string is the valid identifier.

17.islower():
	It returns true if the characters of a string are in lower case, otherwise false.

18.isnumeric():
	It returns true if the string contains only numeric characters.

19.isprintable():
	It returns true if all the characters of s are printable or s is empty, false otherwise.

20.isupper():
	It returns false if characters of a string are in Upper case, otherwise False.

21.isspace():
	It returns true if the characters of a string are white-space, otherwise false.

22.istitle():
	It returns true if the string is titled properly and false otherwise.
	A title string is the one in which the first character is upper-case whereas the other characters are lower-case

23.isupper():
	It returns true if all the characters of the string(if exists) is true otherwise it returns false.

24.join(seq):
	It merges the strings representation of the given sequence.

25.len(string):
	It returns the length of a string.

26.ljust(width[,fillchar]):
	It returns the space padded strings with the original string left justified to the given width.

27.lower():
	It converts all the characters of a string to Lower case.

28.lstrip():
	It removes all leading whitespaces of a string and can also be used to remove particular character from leading.

29.partition():
	It searches for the separator sep in S, and returns the part before it, the separator itself, and the part after it. If the separator is not found, return S and two empty strings.

30.maketrans():
	It returns a translation table to be used in translate function.

31.replace(old,new[,count]):
	It replaces the old sequence of characters with the new sequence.
	The max characters are replaced if max is given

32.rfind(str,beg=0,end=len(str)):
	It is similar to find but it traverses the string in backward direction.

33.rindex(str,beg=0,end=len(str)):
	It is same as index but it traverses the string in backward direction.

34.rjust(width,[,fillchar]):
	Returns a space padded string having original string right justified to the number of characters specified.

35.rstrip():
	It removes all trailing whitespace of a string and can also be used to remove particular character from trailing.

36.rsplit(sep=None, maxsplit = -1):
	It is same as split() but it processes the string from the backward direction.
	It returns the list of words in the string.
	If Separator is not specified then the string splits according to the white-space.

37.split(str,num=string.count(str)):
	Splits the string according to the delimiter str.
	The string splits according to the space if the delimiter is not provided.
	It returns the list of substring concatenated with the delimiter.

38.splitlines(num=string.count('\n')):
	It returns the list of strings at each line with newline removed

39.startswith(str,beg=0,end=len(str)):
	It returns a Boolean value if the string starts with given str between begin and end.

40.strip([chars]):
	It is used to perform lstrip() and rstrip() on the string.

41.swapcase():
	It inverts case of all characters in a string.

42.title():
	It is used to convert the string into the title-case i.e., The string meEruT will be converted to Meerut

43.translate(table,deletechars = ''):
	It translates the string according to the translation table passed in the function .

44.upper():
	It converts all the characters of a string to Upper Case.

45.zfill(width):
	Returns original string leftpadded with zeros to a total of width characters;
	intended for numbers, zfill() retains any sign given (less one zero)

46.string.ascii_letters:
	Concatenation of the ascii_lowercase and ascii_uppercase constants.

47.string.ascii_lowercase:
	Concatenation of lowercase letters

48.string.ascii_uppercase:
	Concatenation of uppercase letters

49.string.digits:
	Digit in strings

50.string.hexdigits:
	Hexadigit in strings

51.string.letters:
	concatenation of the strings lowercase and uppercase

52.string.lowercase:
	A string must contain lowercase letters.

53.string.octdigits:
	Octadigit in a string

54.string.punctuation:
	ASCII characters having punctuation characters.

55.string.printable:
	String of characters which are printable

56.String.endswith():
	Returns True if a string ends with the given suffix otherwise returns False

57.String.startswith():
	Returns True if a string starts with the given prefix otherwise returns False

58.String.isdigit():
	Returns “True” if all characters in the string are digits, Otherwise, It returns “False”.

59.String.isalpha():
	Returns “True” if all characters in the string are alphabets, Otherwise, It returns “False”.

60.string.isdecimal():
	Returns true if all characters in a string are decimal.

61.str.format():
	one of the string formatting methods in Python3, which allows multiple substitutions and value formatting.

62.String.index:
	Returns the position of the first occurrence of substring in a string

63.string.uppercase:
	A string must contain uppercase letters.

64.string.whitespace:
	A string containing all characters that are considered whitespace.

65.string.swapcase():
	Method converts all uppercase characters to lowercase and vice versa of the given string, and returns it

66.replace():
	returns a copy of the string where all occurrences of a substring is replaced with another substring

67.string.Isdecimal:
	Returns true if all characters in a string are decimal

68.String.Isalnum:
	Returns true if all the characters in a given string are alphanumeric.

69.string.Istitle:
	Returns True if the string is a titlecased string

70.String.partition:
	splits the string at the first occurrence of the separator and returns a tuple.

71.String.Isidentifier:
	Check whether a string is a valid identifier or not.

72.String.len:
	Returns the length of the string.

73.String.rindex:
	Returns the highest index of the substring inside the string if substring is found

74.String.Max:
	Returns the highest alphabetical character in a string.

74.String.min:
	Returns the minimum alphabetical character in a string.

75.String.splitlines:
	Returns a list of lines in the string.

76.string.capitalize:
	Return a word with its first character capitalized.

77.string.expandtabs:
	Expand tabs in a string replacing them by one or more spaces

78.string.find:
	Return the lowest indexin a sub string.

79.string.rfind:
	find the highest index.

80.string.count	:
   Return the number of (non-overlapping) occurrences of substring sub in string

81.string.lower:
	Return a copy of s, but with upper case letters converted to lower case.

82.string.split:
	Return a list of the words of the string,If the optional second argument sep is absent or None

83.string.rsplit():
	Return a list of the words of the string s, scanning s from the end.

84.rpartition():
	Method splits the given string into three parts

85.string.splitfields:
	Return a list of the words of the string when only used with two arguments.

86.string.join:
	Concatenate a list or tuple of words with intervening occurrences of sep.

87.string.strip():
	It return a copy of the string with both leading and trailing characters removed

88.string.lstrip:
	Return a copy of the string with leading characters removed.

89.string.rstrip:
	Return a copy of the string with trailing characters removed.

90.string.swapcase:
	Converts lower case letters to upper case and vice versa.

91.string.translate:
	Translate the characters using table

92.string.upper:
	lower case letters converted to upper case.

93.string.ljust:
	left-justify in a field of given width.

94.string.rjust:
	Right-justify in a field of given width.

95.string.center():
	Center-justify in a field of given width.

96.string-zfill:
	Pad a numeric string on the left with zero digits until the given width is reached.

97.string.replace:
	Return a copy of string s with all occurrences of substring old replaced by new.

98.string.casefold():
	Returns the string in lowercase which can be used for caseless comparisons.

99.string.encode:
	Encodes the string into any encoding supported by Python.Default encoding is utf-8.

100.string.maketrans:
	Returns a translation table usable for str.translate()"""
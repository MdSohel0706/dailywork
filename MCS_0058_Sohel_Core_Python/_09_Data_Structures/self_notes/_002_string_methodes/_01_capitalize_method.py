print("--------------------------capitalize()-------------------------------------")
print("capitalize() method converts first character of a string to uppercase"
      " letter and lowercase all other characters")
print("The capitalize()function doesn't take any parameter")

str1 = "hello satish"
print("string is                 :", str1)
str1.capitalize()         # no action here
print("string after capitalize   :", str1.capitalize())  # Hello kumar
str2 = str1.capitalize()
print("string after capitalize   :",str2)                 # Hello kumar

print("--------------3 ways--------------------")
print("--------------way 1---------------------")
# 1 : Current string should be used as is, new string used "one time"
str1 = 'hai satish'
print("normal string is          :", str1)    # hai kumar
print("after capitalize          :",str1.capitalize())  # Hai kumar
print("string is                 :",str1)           # hai kumar

print("--------------way 2----------------------")
# 1 : Current string should be used as is, new string used multiple times"

str1 = "hai satish"
print("normal string is          :", str1)
str2 = str1.capitalize()
print("capitalize string is      :", str2)
print("string is                 :",str1)

print('----------------way3------------------------')
str1= 'hai satish'
print("normal  string is         :",str1)
str1 = str1.capitalize()
print("capitalize string is      :",str1)

name = "hello"
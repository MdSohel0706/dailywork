print("--------------------------count()------------------------------")
print('count() : Counts how many times str occurs in string or in a substring of string.')

str= "python is a high-level programming"
print("normal string is           :", str)
print("normal  string is :  a     :", str.count('a'))
print("normal  string is :  m     :",str.count('m'))
print("normal  string is :  p     :", str.count('p'))
print("normal  string is :  pr    :",str.count('pr'))
print("normal  string is :  h     :", str.count('h'))
print("normal  string is :  high  :",str.count('high'))
print("normal  string is :  on    :", str.count('on'))
print("normal  string is :  is    :",str.count('is'))

print('-----------------slicing------------------')
print("slicing the string: [0:19] :",str.count('h',0,19))
print("slicing the string: [0:19] :",str.count('k',0,19))    # its return 0
# 3 Using Functions  ==> 10
print("--------3 Using Functions----------")
    # I. STATE
message = 'Hello World'
    # BEHAVIOR
def get_str_len(msg):
    print("DEBUG : Given string is : ", msg)
    leng = 0
    for char in msg:
        leng += 1
    print("INFO: Length of given string : ", leng)

get_str_len(message)

# With return type
message = 'Hello World' # Global
def get_str_len(msg):   # msg -> local scope
    print("String is : ",message)  # Global variable can be accesssed from anywhere
    lent = 0            # lent -> Local scope
    for char in msg:
        lent += 1
    return lent
# print(msg, lent) # Local variables cant be accessed from outside fuction

str_len = get_str_len(message)   # x = 10 print(x)
print("Length of given string : ",str_len)

print("Length of given string : ", get_str_len(message))   # print(10)


# Find number is even or odd
x = 10
if x % 2 == 10:
    print("Even number")
else:
    print("Odd number")


# Print even and odd numbers between 1 to 100
# STATE
st = 100 # int(input("Enter start number"))
end = 200 # int(input("Enter end number"))
# BEHAVIOR
def print_even_odd(ini_val, fin_val):   # evenorodd()   evenOrOdd()
    for num in range(ini_val, fin_val+1):
        p = 10
        if num % 2 == 0:
            print("EVen number : ", num)
        else:
            print("Odd number  : ", num)
    print("Number : ", num, p)
# print("Number : ", num, p)
print_even_odd(st, end)



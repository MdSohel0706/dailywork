print("Hello World")


print("------int to float  : Promotion : Implicit casting----------")
x = 10  # 10
print(x, type(x))

x = float(x)  # 10.0  Memory loss
print(x, type(x))
print(10+10.5)  # 10.0+10.5


print("------float to int  : Demotion : Explicit casting----------")
x = 10.5
print(x, type(x))

x = int(x)  # 10 # Data loss
print(x, type(x))


print("------int to string----------")
x = 10  # 10
print(x, type(x))

x = str(x)  # "10" '10'
print(x, type(x))

print("------string to int----------")
x = "1234"
print(x, type(x))

x = int(x)  # 1234
print(x, type(x))

print(int("Hello World"))  # Invalid conversion
n = int(input("Enter the value of n : "))
total = 0
for i in range(2,(n+1)):
    total = total + (n//i)
print(total)
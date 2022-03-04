#creating phonebook file
with open("phonebook.dat","wb") as f:
    n = int(input("Enter the number of entries : "))
    for i in range(n):
        name = input("Enter name : ")
        phno = input("Enter phone number : ")
        name = name.encode()
        phno = phno.encode()
        f.write(name+phno)
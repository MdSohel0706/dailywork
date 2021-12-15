import mmap, sys
print("Enter 1 to display all entries.")
print("Enter 2 to display phone numbers based on name.")
print("Enter 3 to modify an entry based on name.")
print("Enter 4 to exit.")
ch = int(input("Enter choice : "))
if(ch == 4):
    sys.exit()

with open("phonebook.dat","r+b") as f:
    mm = mmap.mmap(f.fileno(),0)
    if(ch == 1):
        print(mm.read().decode())
    elif(ch == 2):
        name = input("Enter name : ")
        n = mm.find(name.encode())
        n1 = n+len(name)
        ph = mm[n1:n1+10]
        print("Phone number = ",ph.decode())
    elif(ch == 3):
        name = input("Enter name : ")
        n = mm.find(name.encode())
        n1 = n + len(name)
        p1 = input("Enter new phone number : ")
        mm[n1:n1+10] = p1.encode()

    mm.close()
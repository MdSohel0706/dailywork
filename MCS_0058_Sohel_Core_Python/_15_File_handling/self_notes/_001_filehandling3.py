import os,sys

fname = input("Enter filename : ")
if(os.path.isfile(fname)):
    f = open(fname,"r")
else:
    print(f"{fname} file doesnt exist.")
    sys.exit()

print("The contents of the file are : ")
str = f.read()
print(str)
f.close()
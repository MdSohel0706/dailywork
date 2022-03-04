#Program to count the number of lines, words and characters in a file
import os, sys
fname = input("Enter filename : ")
if(os.path.isfile(fname)):
    f = open(fname, "r")
else:
    print(fname," file doesnt exits")
    sys.exit()

cl = cw = cc = 0
for line in f:
    words = line.split()
    cl += 1
    cw += len(words)
    cc += len(line)

print("Number of lines = ",cl)
print("Number of words = ",cw)
print("Number of characters = ",cc)
f.close()
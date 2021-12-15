f = open("file1.txt", "a+")
print("Enter the lines to append (@ at the end)")
str = ""
while(str != "@"):
    str = input()
    if(str != "@"):
        f.write(str+"\n")

f.seek(0,0)
print("The contents of the file are : ")
str = f.read()
print(str)
f.close()
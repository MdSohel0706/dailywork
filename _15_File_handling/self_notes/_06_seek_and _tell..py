'''
seek and tell:
To know the position of pointer, use tell() method.
n = f.tell()
n - represents the byte position
f - represents file object

To move file pointer from one point to another, use seek() method.it makes two arguments
f.seek(offset, fromwhere)
offset - represents how many bytes to move
fromwhere- represents 0, 1, 2 0-beginning
f.seek(10, 0)
This will move pointer to 11th byte 10+1  from beginning

f.seek(-10, 2)
This will move the pointer to 9th byte (-10+1) from ending
2 represents ending of file
-10 represents moving back in the file

'''


fi = open("text.txt", "r")
# the second parameter of the seek method is by default 0
fi.seek(30)
# now, we will print the current position
print("current position: ", fi.tell())

print("pointer will start at next position:", fi.readline())
fi.close()




print()
fi = open("text.txt", "r+")
print("Name of the file: ", fi.name)

line_1 = fi.readline()
print("Read Line: %s" % (line_1))

# Again, set the pointer to the beginning
fi.seek(0, 1)
line_2 = fi.readline()
print("Read Line: %s" % (line_2))

# Close opend file
fi.close()




print("__negative offset__")
fi = open("text.txt", "rb")

# the user is setting the reference point to thirtieth position to the left from
# end
fi.seek(-70, 2)

# now print the current position
print(fi.tell())

# now the user will Convert the binary to string
print(fi.readline().decode('utf-8'))

fi.close()

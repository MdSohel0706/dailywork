# working with Binary Files
"""
Binary Files handles data in form of bytes.
It can be used to read images, audio, video files. such as bytes, megabytes, gigabytes
To open a Binary file for reading purpose use 'rb' b(binary) is attached to r(read) represents it is a binary file.
similarly to write a binary file use 'wb' represents w-write, b-bytes
To read bytes from binary file  use read()
To write bytes into binary file use write()

"""

file1 = open('flowers.jpg','rb')
data = file1.read()
file2 = open('myimage.jpg','wb')

file2.write(data)
file1.close()
file2.close()




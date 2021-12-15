# PROGRAM TO READ AND WRITE  DATA FROM A FILE

out_data = open("C:/Users/madhu/Desktop/names.txt", "w")
out_data.write("Welcome to the world of Python")
print("---After writing to file DATA : ", out_data)
out_data.close()

in_data = open("C:/Users/madhu/Desktop/names.txt", "r")
in_data = in_data.read()
print("---Reading from file--------  : ", in_data)
# in_data.close()

obj2 = open("C:/Users/madhu/Desktop/names.txt", "r")
text_data = obj2.read(15)
print("---Reading from file  with byte size : ", text_data)
obj2.close()

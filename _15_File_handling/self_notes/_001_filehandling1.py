'''File opening modes:
w - to write data into a file
r - to read data into a file
a - to append to a file
w+ - to write and read. previous data is deleted
r+ - to read and write data into a file. previous data is not deleted
a+ - to append and read data into a file
x - exclusive creation mode. creation fails if file already exists
rb - read binary file
wb - write binary file
r+b - read and write data from a binary file

PICKLE IN PYTHON
----------------
pickle.dump(object,file)
object = pickle.load(file)

SEEK and TELL
-------------
n = f.tell()
f.seek(offset,fromwhere)

ZIPPING FILES
-------------
f = ZipFile('test.zip','w',ZIP_DEFLATED)
f.write("file1.txt")
f.write("file2.txt")

z = ZipFile("test.zip",'r')
z.extractall()

WORKING WITH DIRECTORIES
------------------------
import os
current = os.getcwd()
os.mkdir('mysub')
os.mkdir('mysub/mysub2')
os.mkdirs('newsub/newsub2')
goto = os.chdir('newsub/newsub2')
os.rmdir('newsub/newsub2')
os.removedirs('mysub/mysub2/mysub3')
os.rename('oldname','newname')
os.walk(path, topdown = True, onerror = None, followlinks = False)
eg.
import os
for dirpath, dirnames, filesnames in os.walk("."):


'''





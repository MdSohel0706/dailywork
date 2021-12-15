import os
print(os.getcwd())
for path, dirs, filenames in os.walk("."):
    print(path)
    print(dirs)
    print(filenames)
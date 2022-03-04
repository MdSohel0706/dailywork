with open("file1.txt","r+b") as f:
    f.write(b'Amazing Python')

    n = f.tell()
    print("Present pointer location = ",n)

    f.seek(5,0)
    n = f.tell()
    print("Present pointer location = ", n)
    print(f.read(2))

    f.seek(-5,2)
    n = f.tell()
    print("Present pointer location = ", n)
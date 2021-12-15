reclen = 20
with open("cities.bin","rb") as f:
    n = int(input("Enter record number : "))
    f.seek((n-1)*reclen)
    str = f.read(20)
    str = str.decode()
    print("Required entry = ",str)

    
with open("cities.bin","rb") as f:
    str = f.read()
    str = str.decode()
    print(str)
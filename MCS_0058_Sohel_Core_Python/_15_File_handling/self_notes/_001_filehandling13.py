import os
reclen = 20
size = os.path.getsize("cities.bin")
n = int(size/reclen)
print("No of records = ",n)
with open("cities.bin","r+b") as f:
    name = input("Enter city name : ")
    name = name.encode()
    new_name = input("Enter new city name : ")
    ln = len(new_name)
    new_name = new_name+(20-ln)*" "
    new_name = new_name.encode()
    position = 0
    found = False
    for i in range(n):
        f.seek(position)
        str = f.read(20)
        if name in str:
            f.seek(-20,1)
            found = True
            f.write(new_name)
            print("Entry updated at position : ",(i+1))
            break
        position += reclen
    if not found:
        print("City not found.")


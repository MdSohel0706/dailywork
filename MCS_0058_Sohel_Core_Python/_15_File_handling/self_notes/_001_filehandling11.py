import os
reclen = 20
city = input("Enter city to find : ")
city = city.encode()
size = os.path.getsize("cities.bin")
n = int(size/reclen)
print("No of records = ",n)
position = 0
found = False
with open("cities.bin","rb") as f:
    for i in range(n):
        f.seek(position)
        str = f.read(20)
        if city in str:
            found = True
            print("City found at record no : ",(i+1))
            break
        position += 20
if not found:
    print("City not found")

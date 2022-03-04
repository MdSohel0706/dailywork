#program to remove specific digit from all elements of a list
l = []
n = int(input("Enter no of elements : "))
for i in range(n):
    l.append(int(input("Enter element : ")))
#list created
req = int(input("Enter digit to remove : "))

final_list = []
for i in l:
    elem = str(i)
    freq = elem.count(str(req))
    final_list.append(elem.replace(str(req),"",freq))

print(final_list)
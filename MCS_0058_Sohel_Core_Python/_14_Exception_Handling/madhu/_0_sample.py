
# Exception handling
'''
Traceback (most recent call last):
  File "C:/Users/madhu/git_projects/Batch_16/B16_PythonTraining/_14_Exception_handling/mypractice/test1.py", line 11, in <module>
    print("Result is ", in_val + 10)
TypeError: must be str, not int
'''
"""
print("--Before list----")
list1 = [1, 2, 3, 4]
print(list1[3])
print("--After list----")
in_val = input("Enter value : ")  # '5'
print("Result is ", in_val + 3)
print("End of program")
"""
"""
print("--Before list----")
list1 = [22, 33, 43, 66]
print(list1[23])
print("--After list----")
in_val = input("Enter value : ")  # '5'
print("Result is ", in_val + 33)
print("End of program")

list2 = [1,2,3,4,5]
list3 =[1,2,3,4,5,]
if(list2 == list3):
 print("well come the satish")
else:
print ("best typelist")"""
"""# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)"""


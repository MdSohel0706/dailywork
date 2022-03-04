import Emp, pickle
f = open("emp.dat","wb")
n = int(input("Enter the number of employees : "))

for i in range(n):
    id = int(input("Enter id : "))
    name = input("Enter name : ")
    salary = int(input("Enter salary : "))

    e = Emp.Emp(id, name, salary)
    pickle.dump(e,f)

f.close()
# CRUD Operations
# C - CREATE -->  When ever we are creating new data.
print("----1. CREATE---------")
eid = 10
sal = 100.43
name = 'Madhu'
name = "Madhu"
is_perm = False

# R - RETRIEVE --> Selects the created data
print("----2. RETRIEVAL------")
print("Empid  :", eid)
print("Name   :", name)
print("Salary :", sal)
print("Emp permanenet ?", is_perm)

# U - UPDATE --> Modify existing data
print("----3. UPDATE------")
sal = 1000.5
name = 'Madhu.N'
is_perm = True

print("Empid  :", eid)
print("Name   :", name)
print("Salary :", sal)
print("Emp permanenet ?", is_perm)

# D - DELETE --> Delete the existing data
print("----4. DELETE ------")
print(eid, name, sal, is_perm)
del eid
print(name, sal, is_perm)
del name
print(sal, is_perm)
del sal
print(is_perm)
del is_perm
# print(is_perm)

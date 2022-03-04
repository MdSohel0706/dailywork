class Emp_A:
    def __init__(self,n):
        self.name = n

class Emp_B:
    def __init__(self, m):
        self.firstname = m

class K(Emp_A,Emp_B):
    def __init__(self,name):
        super().__init__(name)

print(K.mro())
dic1 = {'A':1,'B':2}
dic2 = {"C":3,"D":4}
Kobj = K("Abc")
print(Kobj.name)
#print(Kobj.__getattribute__(name))




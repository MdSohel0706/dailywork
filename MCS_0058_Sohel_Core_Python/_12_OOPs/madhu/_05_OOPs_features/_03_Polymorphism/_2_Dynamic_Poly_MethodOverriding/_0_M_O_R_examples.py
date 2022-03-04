

class A:
    def m1(self):
        print("In A : m1() ")

class B(A):
    def m2(self):
        print("In B :m2()")

a1 = A()
a1.m1()
print("-----------")
b1 = B()
b1.m1()
b1.m2()
#b1.m3()





class A:
    def m1(self):
        print("In A : m1() ")

class B(A):

    def m2(self):
        print("In B :m2()")   # 2

    #method overriding
    def m1(self):
        print("In B :m1()")   # 1.2

a1 = A()
a1.m1()
print("-----------")
b1 = B()
b1.m1()
b1.m2()
#b1.m3()

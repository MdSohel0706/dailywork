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

"""
#Method Resolution Order (MRO)::

In Hybrid Inheritance the method resolution order is decided based on MRO algorithm.
This algorithm is also known as C3 algorithm.
Samuele Pedroni proposed this algorithm.
It follows DLR (Depth First Left to Right)
i.e Child will get more priority than Parent.
Left Parent will get more priority than Right Parent
MRO(X)=X+Merge(MRO(P1),MRO(P2),...,ParentList)

#Head Element vs Tail Terminology:

Assume C1,C2,C3,...are classes.
In the list : C1C2C3C4C5....
C1 is considered as Head Element and remaining is considered as Tail.

#How to find Merge:

Take the head of first list If the head is not in the tail part of any other list,
then add this head to the result and remove it from the lists in the merge.
If the head is present in the tail part of any other list,then consider the
head element of the next list and continue the same process.




#Note: We can find MRO of any class by using mro() function.

print(ClassName.mro())
"""

#example:
class A:pass
class B(A):pass
class C(A):pass
class D(B,C):pass
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())

"""

#Finding mro(P) by using C3 algorithm:
Formula: MRO(X)=X+Merge(MRO(P1),MRO(P2),...,ParentList)

mro(p)= P+Merge(mro(X),mro(Y),mro(C),XYC)
= P+Merge(XABO,YBCO,CO,XYC)
= P+X+Merge(ABO,YBCO,CO,YC)
= P+X+A+Merge(BO,YBCO,CO,YC)
= P+X+A+Y+Merge(BO,BCO,CO,C)
= P+X+A+Y+B+Merge(O,CO,CO,C)
= P+X+A+Y+B+C+Merge(O,O,O)
= P+X+A+Y+B+C+O
"""


class A:pass
class B:pass
class C:pass
class X(A,B):pass
class Y(B,C):pass
class P(X,Y,C):pass
print(A.mro())#AO
print(X.mro())#XABO
print(Y.mro())#YBCO
print(P.mro())#PXAYBCO


class A:
    def m1(self):
        print('A class Method')
class B:
    def m1(self):
         print('B class Method')
class C:
    def m1(self):
        print('C class Method')
class X(A,B):
    def m1(self):
        print('X class Method')
class Y(B,C):
     def m1(self):
        print('Y class Method')
class P(X,Y,C):
    def m1(self):
        print('P class Method')
p=P()
p.m1()
"""
mro(o)=object
mro(D)=D,object
mro(E)=E,object
mro(F)=F,object
mro(B)=B,D,E,object
mro(C)=C,D,F,object
mro(A)=A+Merge(mro(B),mro(C),BC)
=A+Merge(BDEO,CDFO,BC)
=A+B+Merge(DEO,CDFO,C)
=A+B+C+Merge(DEO,DFO)
=A+B+C+D+Merge(EO,FO)
=A+B+C+D+E+Merge(O,FO)
=A+B+C+D+E+F+Merge(O,O)
=A+B+C+D+E+F+O


"""

class D:pass
class E:pass
class F:pass
class B(D,E):pass
class C(D,F):pass
class A(B,C):pass
print(D.mro())
print(B.mro())
print(C.mro())
print(A.mro())

# Python program showing
# how MRO works

class A:
	def rk(self):
		print(" In class A")
class B(A):
	def rk(self):
		print(" In class B")

r = B()
r.rk()


# Python program showing
# how MRO works

class A:
    def rk(self):
        print(" In class A")


class B(A):
    def rk(self):
        print(" In class B")


class C(A):
    def rk(self):
        print("In class C")


# classes ordering
class D(B, C):
    pass


r = D()
r.rk()

#Methods for Method Resolution Order(MRO) of a class:?

# Python program to show the order
# in which methods are resolved

class A:
	def rk(self):
		print(" In class A")
class B:
	def rk(self):
		print(" In class B")

# classes ordering
class C(A, B):
	def _init_(self):
		print("Constructor C")

r = C()

# it prints the lookup order
print(C._mro_)
print(C.mro())

class A:
    def process(self):
        print('A process()')


class B:
    pass


class C(A, B):
    pass


obj = C()
obj.process()
print(C.mro())   # print MRO for class C

#Now, let’s make it a little more complicated by adding process() method to class B also.
class A:
    def process(self):
        print('A process()')


class B:
    def process(self):
        print('B process()')

class C(A, B):
    pass

obj = C()
obj.process()

class A:
    def process(self):
        print('A process()')


class B:
    def process(self):
        print('B process()')


class C(A, B):
    def process(self):
        print('C process()')


class D(C,B):
    pass


obj = D()
obj.process()

print(D.mro())

class A:
    def process(self):
        print('A process()')


class B(A):
    pass


class C(A):
    def process(self):
        print('C process()')


class D(B,C):
    pass


obj = D()
obj.process()


#
#
# class A:
#     def m1(self):
#         print("In A : m1() ")
#
# class B(A):
#     def m2(self):
#         print("In B :m2()")
#
# a1 = A()
# a1.m1()
# print("-----------")
# b1 = B()
# b1.m1()
# b1.m2()
# #b1.m3()

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

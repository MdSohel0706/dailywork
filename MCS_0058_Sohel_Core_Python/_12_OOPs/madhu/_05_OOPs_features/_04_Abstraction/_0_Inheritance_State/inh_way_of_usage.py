print("------1.Normal Inheritance: - 1.1 - Reuse super class methods  AS IS-------")

class A:

    def m1(self):
        print("A  m1()")

    def m2(self):
        print("A  m2()")

class B(A):
    def m3(self):
        print("B  m3()")
b = B()
b.m1()
b.m2()
b.m3()

print("------1.Normal Inheritance: - 1.2 Override super class methods--------")
class A:
    def m1(self):
        print("A  m1()")   # method implementation/method body

    def m2(self):
        print("A  m2()")

class B(A):
    def m1(self):
        print("B  m1()")   # my own implementation

    def m2(self):   # my own implementation
        print("B  m2()")

    def m3(self):
        print("B m3()")

b = B()
b.m1()
b.m2()
b.m3()

print("------1.Normal Inheritance: - 1.3 Few Super classmeethods AS IS, few unique--------")
class A:
    def m1(self):    # Required AS IS in sub class
        print("A  m1()")

    def m2(self):    # Required in unique way in sub class
        print("A  m2()")

class B(A):
    def m3(self):
        print("B  m3()")

b1 = B()
b1.m1()
b1.m2()
b1.m3()


class Pendrive:
    def usb_mesaure(self):
        print("Pendrive  m1()")

class Kingston(Pendrive):
    def usb_mesaure(self):
        print("Pendrive  my own design")



k = Kingston()
k.usb_mesaure()

'''
  1. 2L of Can <== 2L water - YES
  2. 5L of Can <== 5L water - YES
  3. 5L of Can <== 2L water - YES  (Memory Loss)  90%
  4. 2L of Can <== 5L water - NO  (Data Loss) 
x = 10
int x = 10
'''
'''
class Animal:
    def m1()
    
class Tiger(Animal):
    def m2()

Tiger tiger = new Tiger()    # 1    tiger.m1()
                                    tiger.m2()
                                    
Animal animal = new Animal() # 2    animal.m1()
                                        
Animal animal = new Tiger()  # 3**    animal.m1()
                                      animal.m2()  ==> Will give error
                                      

Tiger tiger = new Animal()   # 4    Error Downcasting



x = 10
print(x)  - 10
x = 10.5
print(x)  - 10.5

int x   = 10     # 1
float x = 10.5   # 2
float x = 10     # 3 Implicit casting   ==> float x = (float)10(internally converts)
int x = 10.5  XX # 4 Explict casting    ==> int x = (int)10.5 (externally you have to write)

'''


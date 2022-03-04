class A:
    a = 100
    def __init__(self):
        print("in A init method")
    def m1(self):
        print("A - m1() method")

    def download_file(self):
        print("A - download_file() method ==> pdf ")

class B(A):
    def __init__(self):
        A.__init__(self)
        print("in B init method")

    def m3(self):
        print("B - m3() method")

    def download_file(self):
        print("B - download_file() method ==> excel ")

b = B()
b.m1()
b.download_file()
b.m3()
b.m4()

'''
a = A()
a.m1()
a.m2()
#a.m3()
'''
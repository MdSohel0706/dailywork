'''

'''

'''
  Super class       Sub class
  ================================
class SuperA:      class SubB:
  m1()              0                : Sub class will inherit method from super class
  m1()              m1()             : Sub class overriden inherited method
  m1() m2()         0                : Sub class inherits 2 super class methods
  m1() m2()         m3() m4()        : Sub class inherits 2 super class methods,its own 2 methods
  m1() m2()         m1()* m3() m4()  : Sub class inherits 2 super class methods,its own 2 methods
                                        overriden method m1()
                                        inherited method m2()
                                        own specific methods m3() m4()
                                        
'''


'''

'''

''' OVERRIDE *
II: All sub classes required  : a. Common  signature and 
                                b. unique implementation

                            --> method signature -  common behavior  
                            --> method body      -  unique** implementation 


   If we write classes without inheritance as below,
                 Tiger   		Lion        Cat        Dog
					 eating()    eating()    eating()   eating()
	We cant understand common behavior. 
	So this will not work out.

    ==> We have to use inheritance mechanism here 
    
								Animal
									eating()

                Tiger   		Lion        Cat        Dog
					 eating()    eating()    eating()   eating()

Above mechanism is called as Method Overriding **

'''


class Animal:

    def __init__(self):
        print("SUPER :: Animal constructor")

    def eating(self):
        print("SUPER :: Generic Behavior")  # Generic impl.


class Tiger(Animal):

    def __init__(self):
        print("SUB  :: Tiger constructor")

    def eating(self):  # Method overriding
        print("SUB :: Tiger eating in specific mannaer ")   # specific (our own) impl.

tiger = Tiger()
tiger.eating()

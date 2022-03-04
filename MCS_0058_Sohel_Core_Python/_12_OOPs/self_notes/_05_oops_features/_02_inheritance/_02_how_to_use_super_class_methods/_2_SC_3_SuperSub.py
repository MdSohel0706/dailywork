'''

'''

'''  
SC 3: Few sub classes required 
                     common behavior + 
                     common** implementation   (Tiger,Lion)
      Remaining sub classes required 
                     common behavior(method) + 
                     unique** implementation  (Cat, Dog)


								Animal
									eating()
                Tiger   		Lion        Cat        Dog
					                          eating()   eating()

'''


class Animal:
    def __init__(self):
        pass
        # print("SUPER :: Animal constructor")

    def eating(self):
        print("SUPER :: Animal Generic eating----")


class Tiger(Animal):
    def __init__(self):
        pass
        # print("SUB  :: Tiger constructor")

class Lion(Animal):
    def __init__(self):
        pass
        # print("SUB  :: Lion constructor")

class Cat(Animal):
    def __init__(self):
        pass
        # print("SUB  :: Cat constructor")

    def eating(self):  # Method overriding
        print("SUB :: Cat eating----")

class Dog(Animal):
    def __init__(self):
        pass
        # print("SUB  :: Dog constructor")

    def eating(self):  # Method overriding
        print("SUB :: Dog eating----")

anim = Animal()
anim.eating()

tiger = Tiger()
tiger.eating()

lion = Lion()
lion.eating()

cat = Cat()
cat.eating()

dog = Dog()
dog.eating()

'''

'''

class Animal:
    def __init__(self):
        pass

    def eating(self):
        print("Animal eating")

class Lion(Animal):
    def sleeping(self):
        print("Lion sleeping")

'''
anim = Animal()   # 5L CAN - 5L Water
anim.eating()
anim.sleepgin()N # ERROR

lion = Lion()    # 2L CAN - 2L Water
lion.eating()
lion.sleeping()

5L Can - 5L Water
2L Can - 2L Water


Java, .Net:
---------------

# 1:  5L Can - 5L Water  
Animal anim = Animal()   
anim.eating()
anim.sleepgin()N # ERROR


# 2: # 2L CAN - 2L Water
Lion lion = Lion()    
lion.eating()
lion.sleeping()

# 3: # 5L CAN - 2L Water   -- Upcasting
Animal anim = Lion()
anim.eating()
anim.sleeping()  # ERROR


# 4: 2L Can - 5L Water    -- Downcasting
Lion lion = Animal()   XXX

Lion lion = (Lion)Animal()   XXX


'''
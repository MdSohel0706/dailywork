'''
Instance method have the self as first parameter. Through self they can access the attributes
of the object. Not only can they modify class state with self , but with the help of self.__class__
attribute they can also modify the class state.

Class method have the cls as first parameter. Through cls they can modify the class state, but 
cannot modify instance state.

Static method has neither self nor cls parameter, they can neither access class state or instance state.
They are mainly used for namespacing.


'''

class Myclass:
    def method(self):
        return "Instance method called. ",self

    @classmethod
    def classmethod(cls):
        return "Class method called. ",cls

    @staticmethod
    def staticmethod():
        return "Static method called. "

#Calling instance method
obj = Myclass()
print(obj.method())

#Or we can also call the instance method by passing the object to the method like this
#print(Myclass.method(obj))

#Calling class method
print(obj.classmethod())

print(obj.staticmethod())

print("Without creating object")

print(Myclass.classmethod())
print(Myclass.staticmethod())

#But we cannot call instance method without creating object first.


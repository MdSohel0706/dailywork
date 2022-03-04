from abc import  ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass

    def get_data(self):
        print("get Data : In Polygon")


class Triangle(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I am Quadrilateral with 4 sides")



class Quadrilateral(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I am Quadrilateral with 4 sides")

    # overriding concrete method
    def get_data(self):
        print("Quadrilateral data")


'''
# Perfect example for Abstract class
Abstraction - Hiding implementation details
            - 0 to 100%   - combination of concrete and abstract methods
            - 0%          - all concrete methods
            -100%         - all abstract methods
'''
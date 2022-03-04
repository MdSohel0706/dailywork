from abc import  ABC, abstractmethod

class Polygon(ABC):  # Polygon is abstract class, abstraction 0%

    def noofsides(self):
        print("no of sides : In Polygon ")

    def get_data(self):
        print("get DAta : In Polygon")


class Triangle(Polygon):
    # overriding abstract method
    def get_data(self):
        print("Quadrilateral data")


class Quadrilateral(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I am Quadrilateral with 4 sides")



# Better write Polygon as normal class instead of Abstract class
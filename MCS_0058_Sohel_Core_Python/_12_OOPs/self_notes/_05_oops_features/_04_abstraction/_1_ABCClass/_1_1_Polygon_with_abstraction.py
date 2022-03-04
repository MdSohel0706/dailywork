''''''

'''
                  Polygon
    Triangle Quadrilateral Pentagon Hexagon
    
No abstraction : Methods impl. (all/few) used by sub classes AS IS 
Abstraction : When all methods need to be implemented uniquely in sub classes
              When few methods need to be implemented uniquely in sub classes
              
Abstract class : SC1 : all abstract methods   : 100 % abstraction
                 SC2 : all concrete methods   :  0 % abstraction
                 SC3 : Combination of abstract,concrete methods : 0 to 100% abstraction
                        2 CM, 2 AB -- 50% Abstraction
                        1 CM, 1 AB -- 66.6% abstarction
                        2 CM       -- 0% abstraction
                        1 AM       -- 100% abstraction
   
'''
from abc import ABC, abstractmethod

class Polygon(ABC):    # abstract class ( incomplete)


    @abstractmethod   #decorator
    def noofsides(self):  # abstract method (incomplete method)
        pass

class Quadrilateral(Polygon):

    # method overriding
    def noofsides(self):  # Must and should override super class abstract method
        print("I am Quadrilateral with 4 sides")


class Pentagon(Polygon):
    # overriding
    def noofsides(self):
        print("I am Pentagon with 5 sides")



poly_obj = Polygon()
poly_obj.noofsides()

quad_obj = Quadrilateral()
quad_obj.noofsides()

pent_obj = Pentagon()
pent_obj.noofsides()


print("******************")


'''
We should not write concrete method in super class
Each sub class requires noofsides() behavior impl. in unique way
'''
# Without Abstraction
class Polygon():

    def noofsides(self):
        print("Polygon sides ??????")


class Triangle(Polygon):  #Triangle is a Polygon
    # overriding
    def noofsides(self):
        print("I am Triangle with 3 sides")


class Quadrilateral(Polygon):  #Quadrilateral is a Polygon
    # overriding
    def noofsides(self):
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

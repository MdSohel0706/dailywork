
class Employee:
    # STATE --> data members  *  logical
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    # BEHAVIOR --> member methods   * physical
    def get_details(self):
        print("Employee details")

# Employee.get_details()
obj = Employee(1001,'MadhuN',10000)   # data physical methods logical
obj.get_details()
'''
Class   - Variables - Logical    <===>  Methods  - Physical
Object  - Variables - Physical    <===>  Methods  - Logical
 

'''
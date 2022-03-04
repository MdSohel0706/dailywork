
# Positional arguments

class Employee:
    # Parameterized Constructor
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def getedata(self):
        pass

madhu = Employee(200, 'MadhuN', 10000)

'''
# Defining Constructor
    - Default constructor
    - Parameterized constructor
            - Positional arguments
            - Default arguments
            - keyword arguments

'''
# Default arguments example
class Employee:
    # parameterized constructors
    def __init__(self, eid=None, name=None, sal=None):  # Constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal

    def getedata(self):
        print("Employee info : ", self.eid, self.name, self.sal)


satish = Employee()
satish.getedata()

chandra = Employee(201)
chandra.getedata()

chandra = Employee(201, 'Chandra Sekhar')
chandra.getedata()

sai = Employee(200, 'satish', 10000)
sai.getedata()

farooq = Employee(name='Farooq', sal=20000)
farooq.getedata()

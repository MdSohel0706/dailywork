class Employee:

    def __init__(self, eid, name='Madhu N', sal=1000):  # constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal
        print(self.eid, self.name, self.sal)

# Constructor Overloading

madhu = Employee(100)
madhu = Employee(101, 'Madhu Nettem')
kiran = Employee(102, 'Kiran Kumar', 20000)
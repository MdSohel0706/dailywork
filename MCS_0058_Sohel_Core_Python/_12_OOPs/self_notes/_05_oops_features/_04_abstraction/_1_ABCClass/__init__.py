from abc import ABC, abstractmethod


class Employee(ABC):
    
    def do_something(self):
        print("---Employee class - do_something")
    
class SoftWEmployee(Employee):
    def do_other_thing(self):
        print("---SW Employee class - do_other_thing")
        
    def do_something(self):
        #Employee.do_something(self)
        print("As Software Emp : do_something")
        
emp = Employee()
emp.do_something()

s_emp = SoftWEmployee()
s_emp.do_other_thing()
s_emp.do_something()
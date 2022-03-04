class Emp():
    def __init__(self,id, name, sal):
        self.id = id
        self.name = name
        self.salary = sal

    def display(self):
        print("Emp id = ",self.id,"\nEmp name = ",self.name,"\nEmp salary = ",self.salary)

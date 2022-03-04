

class Employee(object):

    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal

    def get_emp_details(self):
            print("Employee Details are : ",self.id,self.name,self.sal)

    def __str__(self):
        print(self.id,self.name,self.sal)
        return True


li = [1,2,3,4]
print(li) # li.__str__()
li.append()


madhu = Employee(100,'MadhuN',4000)
madhu.get_emp_details()
print(madhu)
print("----------------------------------")
# madhu.__getattribute__()
print("Madhu hash val ",madhu.__hash__())
print("Madhu obj :",madhu)  # madhu.__str__()


'''
str vs repr
init vs new
object class in detail


'''
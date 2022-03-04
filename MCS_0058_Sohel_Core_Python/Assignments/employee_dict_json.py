import json

'''y_dict = {"A":{"id":100,"name":"Sohel","salary":{"Basic":1000,"Special":2000,"HR":3000}},
           "B":{"id":200,"name":"Sasi","salary":{"Basic":500,"Special":1500,"HR":2500},"location": "Bengaluru"}}

with open("C:\\Users\\Sohel\\PycharmProjects\\MCS_0058_Sohel_CorePython\\FILES\\emp_dict.json", "w") as out_file:
    json.dump(my_dict,out_file,indent = 4)
'''
file = open("C:\\Users\\Sohel\\PycharmProjects\\MCS_0058_Sohel_CorePython\\FILES\\emp_dict.json", "r")

my_data = json.load(file)

file.close()

class A:
    def __init__(self,full_dict):
        for class_name in full_dict.keys():
            if(self.__class__.__name__ == class_name):
                emp_details = full_dict[class_name]
                for emp_attr_name in emp_details:
                    setattr(self,emp_attr_name,emp_details[emp_attr_name])

    def show_emp_details(self):
        if(self.id % 2 == 0):
            print("--------------------------------------")
            print("SHOWING EMPLOYEE DETAILS OF ",self.name)
            print("Id : ",self.id)
            print("Name : ",self.name)
            for salary_key in self.salary:
                print(salary_key," = ",self.salary[salary_key])

    def print_payslip(self):
        print("------------------------------------")
        print("Printing Payslip of ",self.name)
        salary_obj = self.salary
        self.net = 0
        for salary_type in salary_obj:
            print(salary_type," = ",salary_obj[salary_type])
            self.net += salary_obj[salary_type]
        print("NET SALARY = ",self.net)

class B(A):
    def __init__(self,my_dict):
        super().__init__(my_dict)

    def show_location(self):
        print("Location = ",self.location)

emp1 = A(my_data)
emp1.show_emp_details()
emp1.print_payslip()
emp2 = B(my_data)
emp2.show_emp_details()
emp2.show_location()
emp2.print_payslip()

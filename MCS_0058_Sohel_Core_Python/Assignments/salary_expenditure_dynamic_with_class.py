class emp:
    def input_salary(self):
        self.name = str(input("Enter name of employee:"))
        self.emp_id = int(input("Enter employee id :"))
        self.basic = float(input("Enter the basic salary of Employee \n"))
        self.hr = float(input("Enter the hr of Employee \n"))
        self.spal = float(input("Enter the special allowences of Employee \n"))
        self.tax = float(input("Enter the tax of Employee \n"))
        self.total_salary = (self.basic + self.hr + self.spal) - self.tax
        return self.total_salary

    def input_expenditure(self):
        flag1 = 1
        self.total_expenditure = 0
        self.total_month = 0
        while(flag1):
            if(flag1 != -1):
                print("--------------------")
                self.month = input("Enter month name : ")
                print("--------------------")
                self.total_month += 1
                flag2 = 1
                while(flag2):
                    if(flag2 != -1):
                        print("--------------------")
                        self.exp_name = input("Enter expenditure name : ")
                        self.exp_cost = int(input("Enter expenditure cost : "))
                        print("--------------------")
                        self.total_expenditure += self.exp_cost
                    another_expenditure = input("Do you want to enter another expenditure (y/n) : ")
                    if(another_expenditure == "y"):
                        flag2 = 1
                    elif(another_expenditure == "n"):
                        flag2 = 0
                    else:
                        print("WRONT INPUT. ENTER EXPENDITURE AGAIN : ")
                        flag2 = -1
            another_month = input("Do you want to enter another month (y/n) : ")
            if (another_month == "y"):
                flag1 = 1
            elif (another_month == "n"):
                flag1 = 0
            else:
                print("WRONT INPUT. ENTER MONTH AGAIN : ")
                flag1 = -1
        return self.total_expenditure,self.total_month
A = emp()
net_income = A.input_salary()
total_expenditure,no_of_months = A.input_expenditure()
total_income = net_income*no_of_months
net_savings = total_income - total_expenditure
print("--------------------")
print("TOTAL INCOME = ",total_income)
print("TOTAL EXPENDITURE = ",total_expenditure)
print("TOTAL SAVINGS = ",net_savings)
print("--------------------")
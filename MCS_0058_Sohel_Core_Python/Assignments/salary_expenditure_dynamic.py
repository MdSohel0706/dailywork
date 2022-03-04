def input_salary():
    name = str(input("Enter name of employee:"))
    emp_id = int(input("Enter employee id :"))
    basic = float(input("Enter the basic salary of Employee \n"))
    hr = float(input("Enter the hr of Employee \n"))
    spal = float(input("Enter the special allowences of Employee \n"))
    tax = float(input("Enter the tax of Employee \n"))
    total_salary = (basic + hr + spal) - tax
    return total_salary

def input_expenditure():
    flag1 = 1
    total_expenditure = 0
    total_month = 0
    while(flag1):
        if(flag1 != -1):
            print("--------------------")
            month = input("Enter month name : ")
            print("--------------------")
            total_month += 1
            flag2 = 1
            while(flag2):
                if(flag2 != -1):
                    print("--------------------")
                    exp_name = input("Enter expenditure name : ")
                    exp_cost = int(input("Enter expenditure cost : "))
                    print("--------------------")
                    total_expenditure += exp_cost
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
    return total_expenditure,total_month

net_income = input_salary()
total_expenditure,no_of_months = input_expenditure()
total_income = net_income*no_of_months
net_savings = total_income - total_expenditure
print("--------------------")
print("TOTAL INCOME = ",total_income)
print("TOTAL EXPENDITURE = ",total_expenditure)
print("TOTAL SAVINGS = ",net_savings)
print("--------------------")
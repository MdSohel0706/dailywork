class salary():
    def __init__(self):
        self.basic = 0
        self.hra = 0
        self.special = 0
        self.tax = 0
        self.net = self.basic+self.hra+self.special-self.tax

    def input_salary(self):
        self.basic = int(input("Enter basic : "))
        self.hra = int(input("Enter hra : "))
        self.special = int(input("Enter special : "))
        self.tax = int(input("Enter tax : "))
        self.net = self.basic+self.hra+self.special-self.tax
        return self.net


class user(salary):
    def __init__(self):
        self.name = ""
        self.empid = ""
        self.net = 0
        self.total_expenditure = 0
        self.total_savings = 0

    def input_user(self):
        self.name = input("Enter name : ")
        self.empid = input("Enter empid : ")
        self.net = super(user,self).input_salary()

    def print_user(self):
        print("------------------------")
        print("NAME : ",self.name)
        print("EMPID : ",self.empid)
        print("NET SALARY : ",self.net)
        print("------------------------")

    '''def print_exp(self, Month_exp):
        for i in Month_exp:
            print(i)'''

    def find_savings(self):
        self.total_expenditure = 0
        n = int(input("Enter number of months : "))
        print("-----------------")
        for i in range(0, n):
            month = input("Enter month name : ")
            print("-----------------")
            m = int(input("Enter the number of expenditure : "))
            print("-----------------")
            #D_exp = {}
            for i in range(0,m):
                exp = input("Enter the name of expenditure : ")
                cost = int(input("Enter the cost : "))
                self.total_expenditure += cost
        print("TOTAL EXPENDITURE = ",self.total_expenditure)
        self.total_savings = (n*self.net) - self.total_expenditure
        print("TOTAL SAVINGS = ",self.total_savings)
        #print_exp(Month_exp)

    '''def calculate_total_expenditure(Month_exp):
        pass'''

    def winner_or_loser(self):
        if(self.total_savings >= 0):
            print("WINNER !!!")
        else:
            print("LOSER !!!")

a = user()
a.input_user()
a.find_savings()
a.print_user()
a.winner_or_loser()




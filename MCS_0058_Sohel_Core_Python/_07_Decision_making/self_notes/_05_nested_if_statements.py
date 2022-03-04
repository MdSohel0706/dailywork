# postitve or negitive or zero

"""num = int(input("enter any number"))
if num >= 0:
    if num > 0:
        print("positive number")
    else:
        print("zero")
else:
    print("negitive number")
"""

"""num =int(input("enter any number:"))
if num<10:
    print(num,'is smaller compare to 10')
    if num==5:
        print("num is equal to ",num)

else:
    print("---the end ---") """

"""               10th exam   
                -----------
L1:            1. PASS                            2. FAIL 
L2:         1.continue     2. disc.           1. retry    2. stop 
L3:    1.Inter   2.Diploma        
L4:  1.MPC  2. BiPC
L5:        1.Govt  2.Pvt 
"""

"""
number = int(input("enter 1 for pass and 2 for fail"))
if number==1:
    print("pass")
    number=int(input("enter 1 for countinue and  2 for desc"))
    if number == 1:
        print("countinue")
        number = int(input("enter 1 for inter and  2 for diploma"))
        if number ==1:
            print("inter")
            number = int(input("enter 1 for mpc  and  2 for bipc" ))
            if number == 1:
                print("mpc")
            else:
                print('bipc')
                number = int(input("enter private or govt"))
                if number == 1:
                    print("govt college")
                else:
                    print("private college")
        else:
            print("diploma")

    else:
        print("discountinue")
else:
    print("Fail")
    number =int(input(" enter 1 for retry or 2 for disc"))
    if number == 1:
        print("retry")
    else:
        print("disc")  """

"""guess = int(input("enter any number between 1 to 10"))
if guess <= 10:
    if guess == 10:
        print("your number is matched with",guess)
    elif guess == 9:
        print("your number is matched with", guess)

else:
    print("plase enter number between 1 to 10") """

"""number = int(input("enter any number"))
guess =  int(input("enter any  guess number:"))
if number > guess:
    print("you enter high number")
elif number < guess:
    print("you enter low number")
else:
    print("matched")
"""

"""guess  = int(input("enter any number between 1 to 10"))
if guess <=10:
    if guess == 10:
        print("matched and your number is",guess)
    if guess == 9:
            print("matched and your number is", guess)


else:
    print("between 1 to 10")
"""
"""
num = int(input("enter any number"))
for i in range(1,11):
    if num == i:
        print("matched , your number is",num)
        break
else:
    print("not matched") """

"""
mobiles ={'lenovo':10000, 'redme' :12000 ,'real_me':15000,'iphone':50000}
for keys,values in enumerate(mobiles,start=1):
    print(keys,values)
    print(mobiles.get('lenovo')) """

"""
age = 19
isGraduated = False
hasLicense = True

# Look if person is 18 years or older
if age >= 18:
    print("You're 18 or older. Welcome to adulthood!")

    if isGraduated:
        print('Congratulations with your graduation!')
    if hasLicense:
        print('Happy driving!') 

licence = True
test_drive =True
licence = True
age =int(input("enter your age"))
if age >=18:
    print("eligible for driving")
    if test_drive:
        print("test the driving")
        if licence:
            print("take the licence")
else:
    print("---the end---")  """

"""
ticket = True
seat = True
ticket = int(input("enter ticket i for  booked and 2 for  not booked "))
if ticket==1:
    print("your booking is confirm")
    if seat:
        print("your seat number is 5")
else:
    print("---not booking-----")
"""
"""
roll_no = int(input("enter your roll number"))
name =input("enter any name ")
marks = int(input("enter your marks"))
if roll_no == 27:
    if name =='kumar':
        if marks>=35:
            print('pass')
        else:
            print("fail")
"""

print("------------------please enter the currect details---------------")

'''name = input("enter your name :")
date_of_birth = int(input("enter your date of birth"))
roll_no = int(input("enter your roll number"))
if name == "kumar":
    if date_of_birth == 1996:
        if roll_no == 27:
            print("name is:", name)
            print("roll number is:", roll_no)
            print("telugu marks  :", 89)
            print("english marks :", 82)
            print("hindi marks   :", 70)
            print("science marks :", 75)
            print("social marks  :", 80)
            print("maths  marks  :", 99)
            print("---pass-----")

        else:
            print("---incorrect roll number----")
    else:
        print("----incorrect date of birth")
else:
    print("---enter currect your name---")'''
def enter_values(n,sub_marks):
    for i in range(0,n):
        sub = input("Enter subject : ")
        marks = int(input("Enter marks : "))
        sub_marks[sub] = marks

def enter_again(n,sub_marks):
    for key,value in sub_marks.items():
        if(value < 75):
            print("Enter marks of subject ",key," : ")
            sub_temp = int(input())
            sub_marks[key] = sub_temp


def grade(sub_marks,n):
    sum = 0
    for i in list(sub_marks.values()):
        sum += i
    avgall = sum*100/(n*100)
    if(avgall > 90):
        print("Average all = ",avgall)
        print("Distinction")
        markslist = list(sub_marks.values())
        print("marklist = ",markslist)
        top1 = max(markslist)
        print("Top1 = ",top1)
        markslist.remove(top1)
        top2 = max(markslist)
        print("Top2 = ", top2)
        markslist.remove(top2)
        top3 = max(markslist)
        print("Top3 = ", top3)
        markslist.remove(top3)
        if(((top1 + top2 + top3)*100/300) > 95):
            print("Gold medal")
    elif(75 < avgall < 90):
        print("Average")
    elif(avgall < 75):
        print("Fail")

n = int(input("Enter the number of subjects : "))
sub_marks = {}
enter_values(n,sub_marks)

count_fail = 0
if(3 <= n <= 7):
    for i in list(sub_marks.values()):
        if(i < 75):
            count_fail += 1
    print("Count fail = ",count_fail)
    if(count_fail==0):
        grade(sub_marks,n)
    elif(count_fail <= 3):
        print("Chance again")
        enter_again(n,sub_marks)
        grade(sub_marks, n)
    else:
        print("FAIL!!!")
elif(n > 7):
    count_fail = 0
    failed = []
    for i in list(sub_marks.values()):
        if(i < 75):
            count_fail += 1
            failed.append(i)
    if(count_fail >= 5):
        print("FAIL IN MORE THAN 4!!!")
        print("DEBARRED !!!")
    else:
        sum = 0
        for j in failed:
            sum += j
        avg = sum*100/((len(failed))*100)
        if(65 <= avg <= 75):
            print("Chance again !!!")
            enter_again(n,sub_marks)
        elif(avg < 65):
            print("FAILED !!!")
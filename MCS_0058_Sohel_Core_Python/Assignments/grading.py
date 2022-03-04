full = int(input("Enter the highest marks : "))
marks_list = []
for i in range(1,7):
    marks_list.append(int(input("Enter marks in subject ")))

marks_list.sort(reverse = True)
print(marks_list)

avg3 = (marks_list[0]+marks_list[1]+marks_list[2])*100/(3*full)
sum = 0
for i in marks_list:
    sum += i
avg = (sum*100)/(6*full)

print("Average score in 6 subjects = ",avg)
print("Average score in top 3 subjects = ",avg3)

if(avg > 90):
    print("Distinction")
    if(avg3 > 95):
        print("Gold medal")
elif(75 < avg < 90):
    print("Average score")
elif(avg < 75):
    print("Fail")


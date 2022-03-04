def purify(my_list):
    empty_set = set()
    i = 0
    while(i<(len(my_list)-1)):
        set1 = set(my_list[i])
        j = i + 1
        duplicate_found = 0
        while(j < len(my_list)):
            set2 = my_list[j]
            if(set1.difference(set2) == empty_set):
                my_list.remove(my_list[j])
                duplicate_found = 1
                break
            j += 1
        if(duplicate_found == 1):
            continue
        else:
            i += 1
    return my_list

print("---------------------------WELCOME ---------------------------")
print("------------------ENTER NUMBERS ONLY. +VE OR -VE.------------- \nENTER \"exit\" TO EXIT PROGRAM")
numbers = []
while(True):
    try:
        n = input("Enter number : ")
        if (n == "exit"):
            break
        numbers.append(float(n))
    except:
        print("Not valid input. Enter integers only : ")
print("-----------------------YOUR NUMBERS ARE ----------------------")
print(numbers)

output_list = []
i = 0
while(i<(len(numbers)-1)):
    j = i+1
    pair_found = 0
    while(j < len(numbers)):
        number1 = numbers[i]
        number2 = numbers[j]
        if((number1+number2) == 7):
            pair_found = 1
            z = (number1,number2)
            output_list.append(z)
            numbers.remove(number1)
            numbers.remove(number2)
            break
        j += 1
    if(pair_found == 1):
        continue
    else:
        i += 1
print("-----------------OUTPUT LIST with DUPLICATES------------------")
print(output_list)

print("-------------------------OUTPUT LIST--------------------------")
purified_list = purify((output_list))
print(purified_list)
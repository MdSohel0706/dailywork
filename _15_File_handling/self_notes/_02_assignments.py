# write the program and fetch data using http get and point out number of holidays in england
# &walesthen group them based on year

"""from urllib.request import urlopen
import json

url = 'https://www.gov.uk/bank-holidays.json'
data = urlopen(url)

data_json = json.loads(data.read())
print(type(data_json))

for key,value in data_json.items():
    if key == "england-and-wales":
        ndata1 = value
        for k,v in ndata1.items():
            if k == 'events':
                ndata2 = v

dic2 = {}
for i in ndata2:
    dic1 = i
    print(dic1['title'],'---- ',dic1['date'] )

"""
"""
import requests
from datetime import datetime
data = requests.get("https://www.gov.uk/bank-holidays.json")
dict1 = (data.json())

#seperate england-and-wales data
data1 = dict1['england-and-wales']

#seperate events data
data2 = data1['events']
#print(data2[0]['date'])

dict1 = {}
#create dictionary by making date at key
for i in range(len(data2)):
    dict1[data2[i]['date']] = data2[i]


#sorting based on date
def func(n): 
    return datetime.strptime(n, '%Y-%m-%d').date()

dict2 = sorted(dict1.keys(), key = func)
#print(dict2)

#seperate the year and use sets to avoid duplicates
dates_set = set()
for i in dict2:
    dates_set.add(i[0 : 4])
#print(dates_set)

#sort the years in ascending order
dates_list = sorted(list(dates_set))
print(dates_list)

#create a dictionary with year as key and year count as value
count_dict = {}

for i in dates_list:
    count = 0
    for key in dict1:
        if key.startswith(i):
            count = count + 1
            count_dict[i] = count
#print(count_dict)

#dispalay the final output
            
for i in dates_list:
    print('\n------------------------', i,' has', count_dict[i], ' holidays------------------------ \n')
    for key in dict1:
        if key.startswith(i):
            print(key, dict1[key])
  """
"""write the program and fetch data using http get and point out number of holidays in england
&walesthen group them based on year"""

# Export the json data into csv file by using url
import json
"""import csv
with open("https://www.gov.uk/bank-holidays.json") as file:
    csv_file = csv.writer(file)
    csv_file.writerow([])
    for item in data["result"]"""

# write the program and fetch data using http get and point out number of holidays in england
# &walesthen group them based on year

"""from urllib.request import urlopen
import json

url = 'https://www.gov.uk/bank-holidays.json'
data = urlopen(url)

data_json = json.loads(data.read())
print(type(data_json))

for key,value in data_json.items():
    if key == "england-and-wales":
        ndata1 = value
        for k,v in ndata1.items():
            if k == 'events':
                ndata2 = v

dic2 = {}
for i in ndata2:
    dic1 = i
    print(dic1['title'],'---- ',dic1['date'] )

"""
"""
import requests
from datetime import datetime
data = requests.get("https://www.gov.uk/bank-holidays.json")
dict1 = (data.json())

#seperate england-and-wales data
data1 = dict1['england-and-wales']

#seperate events data
data2 = data1['events']
#print(data2[0]['date'])

dict1 = {}
#create dictionary by making date at key
for i in range(len(data2)):
    dict1[data2[i]['date']] = data2[i]


#sorting based on date
def func(n): 
    return datetime.strptime(n, '%Y-%m-%d').date()

dict2 = sorted(dict1.keys(), key = func)
#print(dict2)

#seperate the year and use sets to avoid duplicates
dates_set = set()
for i in dict2:
    dates_set.add(i[0 : 4])
#print(dates_set)

#sort the years in ascending order
dates_list = sorted(list(dates_set))
print(dates_list)

#create a dictionary with year as key and year count as value
count_dict = {}

for i in dates_list:
    count = 0
    for key in dict1:
        if key.startswith(i):
            count = count + 1
            count_dict[i] = count
#print(count_dict)

#dispalay the final output

for i in dates_list:
    print('\n------------------------', i,' has', count_dict[i], ' holidays------------------------ \n')
    for key in dict1:
        if key.startswith(i):
            print(key, dict1[key])
  """
"""write the program and fetch data using http get and point out number of holidays in england
&walesthen group them based on year"""

# Export the json data into csv file by using url
"""import json
"""
"""import csv
with open("https://www.gov.uk/bank-holidays.json") as file:
    csv_file = csv.writer(file)
    csv_file.writerow([])
    for item in data["result"]"""

# write the program and fetch data using http get and point out number of holidays in england
# &walesthen group them based on year

"""from urllib.request import urlopen
import json

url = 'https://www.gov.uk/bank-holidays.json'
data = urlopen(url)

data_json = json.loads(data.read())
print(type(data_json))

for key,value in data_json.items():
    if key == "england-and-wales":
        ndata1 = value
        for k,v in ndata1.items():
            if k == 'events':
                ndata2 = v

dic2 = {}
for i in ndata2:
    dic1 = i
    print(dic1['title'],'---- ',dic1['date'] )

"""
"""
import requests
from datetime import datetime
data = requests.get("https://www.gov.uk/bank-holidays.json")
dict1 = (data.json())

#seperate england-and-wales data
data1 = dict1['england-and-wales']

#seperate events data
data2 = data1['events']
#print(data2[0]['date'])

dict1 = {}
#create dictionary by making date at key
for i in range(len(data2)):
    dict1[data2[i]['date']] = data2[i]


#sorting based on date
def func(n): 
    return datetime.strptime(n, '%Y-%m-%d').date()

dict2 = sorted(dict1.keys(), key = func)
#print(dict2)

#seperate the year and use sets to avoid duplicates
dates_set = set()
for i in dict2:
    dates_set.add(i[0 : 4])
#print(dates_set)

#sort the years in ascending order
dates_list = sorted(list(dates_set))
print(dates_list)

#create a dictionary with year as key and year count as value
count_dict = {}

for i in dates_list:
    count = 0
    for key in dict1:
        if key.startswith(i):
            count = count + 1
            count_dict[i] = count
#print(count_dict)

#dispalay the final output

for i in dates_list:
    print('\n------------------------', i,' has', count_dict[i], ' holidays------------------------ \n')
    for key in dict1:
        if key.startswith(i):
            print(key, dict1[key])
  """
"""write the program and fetch data using http get and point out number of holidays in england
&walesthen group them based on year"""

# Export the json data into csv file by using url
import json

"""import csv
with open("https://www.gov.uk/bank-holidays.json") as file:
    csv_file = csv.writer(file)
    csv_file.writerow([])
    for item in data["result"]"""

# write the program and fetch data using http get and point out number of holidays in england
# &walesthen group them based on year

"""from urllib.request import urlopen
import json

url = 'https://www.gov.uk/bank-holidays.json'
data = urlopen(url)

data_json = json.loads(data.read())
print(type(data_json))

for key,value in data_json.items():
    if key == "england-and-wales":
        ndata1 = value
        for k,v in ndata1.items():
            if k == 'events':
                ndata2 = v

dic2 = {}
for i in ndata2:
    dic1 = i
    print(dic1['title'],'---- ',dic1['date'] )

"""
"""
import requests
from datetime import datetime
data = requests.get("https://www.gov.uk/bank-holidays.json")
dict1 = (data.json())

#seperate england-and-wales data
data1 = dict1['england-and-wales']

#seperate events data
data2 = data1['events']
#print(data2[0]['date'])

dict1 = {}
#create dictionary by making date at key
for i in range(len(data2)):
    dict1[data2[i]['date']] = data2[i]


#sorting based on date
def func(n): 
    return datetime.strptime(n, '%Y-%m-%d').date()

dict2 = sorted(dict1.keys(), key = func)
#print(dict2)

#seperate the year and use sets to avoid duplicates
dates_set = set()
for i in dict2:
    dates_set.add(i[0 : 4])
#print(dates_set)

#sort the years in ascending order
dates_list = sorted(list(dates_set))
print(dates_list)

#create a dictionary with year as key and year count as value
count_dict = {}

for i in dates_list:
    count = 0
    for key in dict1:
        if key.startswith(i):
            count = count + 1
            count_dict[i] = count
#print(count_dict)

#dispalay the final output

for i in dates_list:
    print('\n------------------------', i,' has', count_dict[i], ' holidays------------------------ \n')
    for key in dict1:
        if key.startswith(i):
            print(key, dict1[key])
  """
"""write the program and fetch data using http get and point out number of holidays in england
&walesthen group them based on year"""

# Export the json data into csv file by using url
"""import json"""

"""
import csv
with open("https://www.gov.uk/bank-holidays.json") as file:
    csv_file = csv.writer(file)
    csv_file.writerow([])
    for item in data["result"]
    """


"""
import json
import pandas as pd
df = pd.read_json("https://www.gov.uk/bank-holidays.json")
f = open('satish.csv', 'w')
df.to_csv('satish.csv')
"""

"""
dave = [180]
owen = [50]
amr = [150]
laura = [360]
vic = [0]

dave.append(dave[-1] - 180)
laura.append(laura[-1] + 180/3)
owen.append(owen[-1] + 180/3)
vic.append(vic[-1] + 180/3)

owen.append(owen[-1] - 50)
dave.append(dave[-1] + 50)

amr.append(amr[-1] - 150)
vic.append(vic[-1] + 150/2)
owen.append(owen[-1] + 150/2)

laura.append(laura[-1] - 360)
amr.append(amr[-1]+ 360/2)
vic.append(vic[-1] + 360/2)

print(f"Dave {dave[-1]}, Laura {int(laura[-1])}, Owen {int(owen[-1])}, Vic {int(vic[-1])}, Amr {int(amr[-1])}")

"""

# create user with name,empid, total salary --->user input
# total salary  contains basic, HRA,special allowance,tax--->variable each month
# net salary = basic + HRA+ special-tax --->tax
# expenditure name & amount -user iput ---> variable each month
# net salary -expenditure = total savings
# -ve value -loser +ve value -winner

"""name = input("Enter the name :")
employee_id = int(input("Enter the employeeid :"))
total_salary = int(input("Enter the  Total salary :"))"""











"""
import random"""
"""
using OOPs concept. 
Class is a blueprint of an object. 
Object is derived from class. 
It is an instance of the class. 
Which means class is a copy of object. 
An object of a class has the same attributes and functions of a class.
"""
#creating a class of a real world object
#creating class Card
"""class Card:
    #_init_ function is called when object of class is created
    def _init_(self,a,b):#whenever an object encounters self it points to itself(i.e. that object only)
        self.suit = a #creating suit attribute of class Card
        self.value = b #creating value attribute of class Card

    def show_card(self): #function to display a card
        if(2 <= self.value <= 10):
            print(self.value," of ",self.suit)
        elif(self.value == 1):
            print("A of ",self.suit)
        elif(self.value == 11):
            print("J of ",self.suit)
        elif(self.value == 12):
            print("Q of ",self.suit)
        elif (self.value == 13):
            print("K of ", self.suit)
#creating a class of a real world object called Deck
class Deck():
    def _init_(self):
        self.cards = []
        self.build()

    #function to build the deck
    def build(self):
        for s in ("Clubs","Spades","Diamonds","Hearts"):
            for v in range(1,14):
                #print("s = ",s," v = ",v)
                self.cards.append(Card(s,v))

    #function to show the deck
    def show_deck(self):
        print("-------------SHOWING DECK OF SHUFFLED CARDS---------")
        for i in self.cards:
            i.show_card()
        print("----------------------------------------------------")

    #function to shuffle the deck
    def shuffle(self):
        for i in range((len(self.cards)-1),0,-1):
            j = random.randint(0,i)
            self.cards[i],self.cards[j] = self.cards[j],self.cards[i]

    #function to draw a card
    def draw_card(self):
        return self.cards.pop()

#creating a player class
class Player():
    def _init_(self, name):
        self.name = name
        self.hand = []

    #function to show name of player
    def show_name(self):
        return self.name

    #function for player to draw a card
    def draw(self,Deck):
        self.hand.append(Deck.draw_card())

    #function to show player's hand
    def show_hand(self):
        print("SHOWING HAND OF ",self.show_name(),"-------------")
        for card in self.hand:
            card.show_card()

    #function to display sum of the cards in hand
    def display_sum_of_hand(self):
        sum = 0
        for card in self.hand:
            sum += card.value
        print("For player ",self.show_name())
        print("SUM OF HAND = ",sum)

    #function to return sum of cards in hand
    def return_sum_of_hand(self):
        sum = 0
        for card in self.hand:
            sum += card.value
        return sum

#creating a game class
class Game():

    def _init_(self,p1,p2):
        self.player1 = Player(p1)
        self.player2 = Player(p2)
        self.players = [self.player1,self.player2]

    #function to shuffle players
    def shuffle_players(self):
        first =  random.randint(1,3)
        if(first == 2):
            self.players[0],self.players[1] = self.players[1],self.players[0]
        print(self.players[0].show_name()," goes first : ")

    #function to distribute cards to players
    def distribute(self,Deck):
        for i in range(1,27):
            for p in self.players:
                p.draw(Deck)
    #function to show players hand after distributing cards
    def show_after_distribute(self):
        for player in self.players:
            player.show_hand()
    #function to display sum of cards
    def sum_of_cards(self):
        for player in self.players:
            player.display_sum_of_hand()
     #function to display who is winner
    def WINNER_AND_LOSER(self):
        sum1 = self.players[0].return_sum_of_hand()
        sum2 = self.players[1].return_sum_of_hand()
        if(sum1 > sum2):
            print(self.players[0].show_name()," IS WINNER!!!")
        else:
            print(self.players[1].show_name(), " IS WINNER!!!")
"""
#creating objects through players
"""CONTESTANT1 = input("Enter player 1 name : ")
CONTESTANT2 = input("Enter player 2 name : ")
game_object = Game(CONTESTANT1,CONTESTANT2)
deck_object = Deck()
deck_object.shuffle()
deck_object.show_deck()
game_object.shuffle_players()
game_object.distribute(deck_object)
game_object.show_after_distribute()
game_object.sum_of_cards()
game_object.WINNER_AND_LOSER()
"""

#card1 = Card("Diamond",1)
#card1.show_card()"""

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
        numbers.append(int(n))
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
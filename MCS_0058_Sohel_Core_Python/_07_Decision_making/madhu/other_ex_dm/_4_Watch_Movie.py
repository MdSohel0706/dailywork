'''
REQUIREMENT
movie watch
theater
netflix
tv
'''

choice = input("Enter your choice from 1. theater 2. netflix 3. tv ::")

if choice =='theater':
    th_open = input("Theaters opened or not 1. YES 2. NO ")
    if th_open == 'YES':
        print("Go and watch the movie in THEATER")
    else:
        print("Sorry you can't")
elif choice == 'netflix':
    subscribed = input("Are you subscribed or not: 1. YES 2. NO")
    if subscribed == 'YES':
        print("Ok watch the movie in NETFLIX")
    else:
        print("Please activate account")
else:
    power = input("Current at home ? 1. ON 2. OFF")
    if power == 'ON':
        print("Watch the movie in TV")
    else:
        print("Please wait for power")

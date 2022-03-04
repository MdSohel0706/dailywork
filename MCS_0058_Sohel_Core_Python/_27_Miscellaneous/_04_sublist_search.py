class Node:
    def __init__(self, val):
        self.value = val
        self.next = None 

class LinkedList:
    def __init__(self):
        self.start = None
        self.current = self.start
    
    def enter_node(self, value):
        if(self.start == None):
            self.start = Node(value)
            self.current = self.start
        else:
            self.current = self.start
            while(self.current.next != None):
                self.current = self.current.next 
            self.current.next = Node(value)

    def print_list(self):
        print("*"*20)
        self.current = self.start
        while(self.current != None):
            print(self.current.value, '->', end = '')
            self.current = self.current.next
        print("None")
        print("*"*20)

    def search_list(self, list2):
        found = False
        self.current = self.start 
        while(self.current != None):
            if(found == True):
                break
            index = self.current.next
            list2.current = list2.start
            while(True):
                if(list2.current == None):
                    print("LIST FOUND")
                    found = True
                    break 
                if(self.current.value == list2.current.value):
                    self.current = self.current.next 
                    list2.current = list2.current.next 
                elif(self.current.value != list2.current.value):
                    self.current = index 
                    break
        if(found == False):
            print("LIST NOT FOUND")

def mayne():
    list1 = LinkedList()
    print("*"*20,"\nEnter List 1 : ")
    print("*"*20)
    while(True):
        print("\n","*"*19,"\nEnter 1 to enter node.\nEnter 2 to print list.\nEnter 3 to stop.\n","*"*19,"\n")
        choice = int(input("Enter choice : "))
        if(choice == 1):
            val = int(input("Enter value to insert : "))
            list1.enter_node(val)
        elif(choice == 2):
            print("\nDISPLAYING LIST 1")
            list1.print_list()
        elif(choice == 3):
            break

    print("*"*20,"\nEnter list 2 : \n","*"*20,"\n")
    list2 = LinkedList()
    while(True):
        print("\n","*"*10,"\nEnter 1 to enter node. Enter 2 to print list. Enter 3 to stop.\n","*"*10)
        choice = int(input("Enter choice : "))
        if(choice == 1):
            val = int(input("Enter value to insert : "))
            list2.enter_node(val)
        elif(choice == 2):
            print("\nDISPLAYING LIST 2")
            list2.print_list()
            print("\n---------------------")
        elif(choice == 3):
            break
    
    print("\nLIST 1 : ")
    list1.print_list()
    print("\nLIST 2 : ")
    list2.print_list()
    print("\nSEARCHING LIST 2 IN LIST 1")
    list1.search_list(list2)
            
mayne()

    
    


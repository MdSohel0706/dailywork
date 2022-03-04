class Node:
    def __init__(self, value):
        self.data = value
        self.next = None 

class LinkedList:
    def __init__(self):
        self.start = None
        self.current = None

    def length_of_list(self):
        if(self.start == None):
            length = 0
        else:
            length = 1
            self.current = self.start 
            while(self.current.next != None):
                length += 1
                self.current = self.current.next
        return length

    def reclen(self, curr):
        if(curr.data == None):
            return 0
        else:
            return 1+(self.reclen(curr.next))
    
    def insert_node(self,value):
        if(self.start == None):
            self.start = Node(value)
            self.current = self.start
        else:
            self.current = self.start 
            while(self.current.next != None):
                self.current = self.current.next
            self.current.next = Node(value)
    
    def delete_node(self,value):
        found = False
        if(self.start != None):
            if(self.start.data == value):
                self.start = self.start.next 
                print("{} deleted.".format(value))
            else:
                self.current = self.start
                while(self.current.next != None):
                    if(self.current.next.data == value):
                        self.current.next = self.current.next.next
                        found = True
                        break
                    self.current = self.current.next
                if(found == True):
                    print("{} deleted.".format(value))
                else:
                    print("Value not in list.")
        else:
            print("List empty. Nothing to delete.")

    def delete_node_by_index(self, index):
        if(self.start == None):
            print("List empty. Nothing to delete.")
        elif(index > self.length_of_list()):
            print("Position greater than length of list.")
        elif(index == 1):
            print("{} deleted.".format(self.start.data))
            self.start = self.start.next
        else:
            self.current = self.start 
            posi = 1
            while(posi < index-1):
                self.current = self.current.next 
                posi += 1
            print("{} deleted.".format(self.current.next.data))
            self.current.next = self.current.next.next
                
    def print_list(self):
        self.current = self.start 
        while(self.current != None):
            print(self.current.data, " -> ", end = "")
            self.current = self.current.next
        print("None")

L = LinkedList()
while(True):
    print("*"*40)
    ch = input("Enter 1 to insert node, 2 to display list, 3 to delete, 4 to delete by position, 5 to print length of list, x to exit, 6 to find length by recursive way : ")
    print("*"*40)
    if(ch == 'x'):
        break 
    elif(ch == '1'):
        val = int(input("Enter value to insert : "))
        L.insert_node(val)
    elif(ch == '2'):
        L.print_list()
    elif(ch == '3'):
        value = int(input("Enter value to delete : "))
        L.delete_node(value)
    elif(ch == '4'):
        value = int(input("Enter position at which to delete : "))
        L.delete_node_by_index(int(value))
    elif(ch == '5'):
        print(L.length_of_list())
    elif(ch == '6'):
        print(L.reclen(L.start))
        
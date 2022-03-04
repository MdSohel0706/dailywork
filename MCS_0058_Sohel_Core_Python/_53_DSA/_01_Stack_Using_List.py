'''
Complexity Analysis:
Push and Pop have a complexity of O(1).
Uses:
1. Website page storage stack, use of back button in web browser.
2. Stacks are used in compilers to calculate expressions by converting them into prefix and postfix.
'''

class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return not(self.stack)

    def push(self,val):
        self.stack.append(val)

    def pop(self):
        if(not(self.is_empty())):
            return self.stack.pop()
        else:
            print("Nothing to pop.")

    def peek(self):
        return self.stack[-1]

    def print_stack(self):
        print(self.stack)

stack = Stack()

while(True):
    ch = int(input("Enter 1 to push, 2 to pop, 3 to peek, 4 to check if empty, 5 to print stack, 6 to exit : "))
    if(ch == 1):
        val = int(input("Enter value : "))
        stack.push(val)
    if(ch == 2):
        print("Popped element = ",stack.pop())
    if(ch == 3):
        print("Top element = ",stack.peek())
    if(ch == 4):
        print(stack.is_empty())
    if(ch == 5):
        stack.print_stack()
    if(ch == 6):
        break

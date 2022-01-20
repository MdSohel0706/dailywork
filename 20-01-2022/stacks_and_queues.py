'''
Data Structures in Python: Stacks, Queues, Linked Lists


ADTs vs Data Structures
Before moving on, it’s important you know the difference between two similar (but very different) words:   ADT and Data Structure.

ADT (Abstract Data Type) – a ‘model’ or a ‘blueprint’ for a data structure. It defines which functions or operations a data structure must have to be considered as such. The benefits of ADTs are that it is much easier to understand since you are seeing a “high-level” overview, instead of getting bogged down in the “low-level” code.
Data Structure – the implementation of an Abstract Data Type. They are the building blocks of any piece of software. It can be defined as a group of data elements that provide a structured way of storing and organizing data so that it can be used efficiently. Different data structures serve different purposes, and as a computer scientist, it is your job to know the pros and cons and ins and outs of each data structure (so that you may pick the right one for the job). This blog article should be seen as an intro to the subject and not a complete essay regarding each data type. For that, I recommend Mosh’s “Ultimate Data Structures and Algorithms Course”.
“Data Structures” (at University) is known as a ‘weed-out’ class, and that’s not without good reason. For many, it is very difficult to visualize something that isn’t there. But I say anyone can do it. That’s right, anyone! All it takes is practice, practice, practice. Are you getting it yet? PRACTICE! Without further adieu, let’s get into it!

Stacks
Stacks -the simplest of all data structures, but also the most important. A stack is a collection of objects that are inserted and removed using the LIFO principle. LIFO stands for “Last In First Out”. Because of the way stacks are structured, the last item added is the first to be removed, and vice-versa: the first item added is the last to be removed.
You can think of Stacks like a PEZ candy dispenser. You put the candy into the dispenser, and once it is full, you start taking the candy back out. BUT, the last piece added is the first piece that comes back out. That is the perfect example of LIFO.

Stack’s ADT Operations:
A ‘Stack‘ is an ADT such that S (stack) supports the following methods:

S.push(e): Adds an element to the top of stack S.
S.pop(): Removes and returns the element from the top of stack S. Error occurs if empty.
S.peek(): Returns a reference to the top of stack S without removing it. Error occurs if empty.
S.is_empty(): Returns True if no elements found in stack S, else returns False
S.size(): Returns the number of elements in stack S.

Adapter Pattern
Though some would assume that a list in Python is synonymous with a Stack Data Structure, it is not the case. The python list includes behaviors that are not included in the Stack ADT. Also, much of the terminology for the function names are different.

When we want to modify an existing class so that its methods match those of a related but different class or interface, we can use the adapter design pattern. Let’s code a class called StackADT that extends the Python list class. Its underlying data will use a list, but the method names that use the list class will all be named after the methods in the Stack ADT.

Stack Data Structure
Are you following me so far? I know it’s a lot to take in, but bear with me! You’ll be using Data Structures in no time. As we talked about before, a Data Structure is the implementation of an ADT in code.

Here is the code for a stack with the functions from its ADT:

# LIFO Stack implementation using a Python list as
# its underlying storage.
'''
class StackADT:
    # Create an empty stack.
    def __init__(self):
        self.data = []

    # Add element e to the top of the stack
    def push(self, e):
        self.data.append(e)

    # Remove and return the element from the top of the stack
    # (i.e., LIFO). Raise exception if the stack is empty.
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self.data.pop()

    # Return (but do not remove) the element at the top of
    # the stack. Raise Empty exception if the stack is empty.
    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self.data[-1]

    # Return True if the stack is empty.
    def is_empty(self):
        return len(self.data) == 0

    # Return the number of elements in the stack.
    def size(self):
        return len(self.data)


S = StackADT()
S.push("S")
S.push("T")
S.push("A")
S.push("C")
S.push("K")
S.peek()       # K
S.size()       # 5
S.is_empty()   # False
S.pop()        # K
S.pop()        # C
S.pop()        # A
S.pop()        # T
S.pop()        # S
S.is_empty()   # True
S.size()       # 0
S.peek()       # IndexError: Stack is empty
 

'''
I’m sure you noticed that when we pushed an item onto the stack, then pushed another, the original item got buried deeper and deeper. Then, when we popped an item off the top of the stack, the most recent item that we added was the first to be returned. That’s because it follows the LIFO (Last In First Out) pattern.

Queues
Queues – essentially a modified stack. It is a collection of objects that are inserted and removed according to the FIFO (First In First Out) principle. Queues are analogous to a line at the grocery store: people are added to the line from the back, and the first in line is the first that gets checked out – BOOM, FIFO! 
Items are added to the back and removed from the front. Simple, right? A queue would be a great data structure to handle incoming calls to a business, or an online shopping store!
Figure 2.1: A Checkout Line Is FIFO



Queue’s ADT Operations:
A queue is a collection of objects where access and deletion are limited to the first element and where insertion is limited to the back of the queue. This rule enforces the FIFO principle.

A ‘Queue‘ is an ADT such that Q (queue) supports the following methods:

S.enqueue(e): Adds an element to the back of queue Q..
S.dequeue(): Removes and returns the first element from queue Q. Error occurs if empty.
S.peek(): Returns a reference to the first element of queue Q without removing it. Error occurs if empty.
S.is_empty(): Returns True if no elements found in queue Q, else returns False
S.size(): Returns the number of elements in queue Q.

Queue’s Data Structure
Now that we’ve covered the methods that a queue must possess, let’s get into writing some code! If you’ve made it this far, pat yourself on the back because you’re one step closer to mastering data structures – the backbone of computer science.

Here is the code for a queue with the functions from its ADT:

 '''

# FIFO Queue implementation using a Python list as
# its underlying storage.
class QueueADT:
    # Create an empty queue.
    def __init__(self):
        self.data = []

    # Add element e to the back of the queue
    def enqueue(self, e):
        self.data.insert(0, e)

    # Remove and return the element from the front of the queue
    # (i.e., FIFO). Raise exception if the queue is empty.
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        else:
            return self.data.pop()

    # Return (but do not remove) the first element of the
    # queue. Raise exception if the queue is empty.
    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        else:
            return self.data[-1]

    # Return True if the queue is empty.
    def is_empty(self):
        return len(self.data) == 0

    # Return the number of elements in the queue.
    def size(self):
        return len(self.data)


Q = QueueADT()
Q.enqueue("Q")
Q.enqueue("U")
Q.enqueue("E")
Q.enqueue("U")
Q.enqueue("E")
Q.peek()         # Q
Q.size()         # 5
Q.is_empty()     # False
Q.dequeue()      # Q
Q.dequeue()      # U
Q.dequeue()      # E
Q.dequeue()      # U
Q.dequeue()      # E
Q.is_empty()     # True
Q.size()         # 0
Q.peek()         # IndexError: Queue is empty
 
'''
Notice how in the enqueue method, I didn’t just append the item to the end of the list? That would have merely added the item to the end of the queue, defeating its entire purpose. Instead, we insert the item at the first position in the list. This follows the queue Abstract Data Type and ensures that it follows the FIFO (first in first out) pattern.
Then in the dequeue method, the item is removed and returned from the front of the list, just like a line at the grocery store. See! It’s not that bad once we chunk it down and use analogies! The key to mastering any subject is to have a firm grasp on the fundamentals, and programming is NO different.
Linked Lists
The Stack and Queue representations I just shared with you employ the python-based list to store their elements. A python list is nothing more than a dynamic array, which has some disadvantages.

The length of the dynamic array may be longer than the number of elements it stores, taking up precious free space.
Insertion and deletion from arrays are expensive since you must move the items next to them over
Using Linked Lists to implement a stack and a queue (instead of a dynamic array) solve both of these issues; addition and removal from both of these data structures (when implemented with a linked list) can be accomplished in constant O(1) time. This is a HUGE advantage when dealing with lists of millions of items.

Linked Lists – comprised of ‘Nodes’. Each node stores a piece of data and a reference to its next and/or previous node. This builds a linear sequence of nodes. All Linked Lists store a head, which is a reference to the first node. Some Linked Lists also store a tail, a reference to the last node in the list.
*Note: Linked Lists do not have a “set-in-stone” set of operations. Linked Lists are merely data structures used to create other ADTs/data structures, such as Stacks or Queues.

Stack: Implemented From a Linked List
The operations for a stack made from a linked list are the same as the operations from a stack made from an array.

The Code
'''
# LIFO Stack implementation using a linked list 
# as its underlying storage
class LinkedListStack:
    # ----------------------Nested Node Class ----------------------

    # This Node class stores a piece of data (element) and
    # a reference to the Next node in the Linked List
    class Node:
        def __init__(self, e):
            self.element = e
            self.next = None   # reference to the next Node

# ---------------------- stack methods -------------------------
    # Create an empty stack
    def __init__(self):
        self._size = 0
        # reference to head node (top of stack)
        self.head = None

    # Add element e to the top of the stack.
    def push(self, e):
        # New node inserted at Head
        newest = self.Node(e)
        newest.next = self.head
        self.head = newest
        self._size += 1

    # Remove and return the element from the top of the stack
    # (i.e., LIFO). Raise exception if the stack is empty.
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')

        elementToReturn = self.head.element
        self.head = self.head.next
        self._size -= 1

        return elementToReturn

    # Return (but do not remove) the element at the top of
    # the stack. Raise Empty exception if the stack is empty.
    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.head.element

    # Return True if the stack is empty.
    def is_empty(self):
        return self._size == 0

    # Return the number of elements in the stack.
    def size(self):
        return self._size


LLS = LinkedListStack()
LLS.push("L")
LLS.push("L")
LLS.push("S")
LLS.push("T")
LLS.push("A")
LLS.push("C")
LLS.push("K")
LLS.peek()       # K
LLS.size()       # 7
LLS.is_empty()   # False
LLS.pop()        # K
LLS.pop()        # C
LLS.pop()        # A
LLS.pop()        # T
LLS.pop()        # S
LLS.pop()        # L
LLS.pop()        # L
LLS.is_empty()   # True
LLS.size()       # 0
LLS.peek()       # IndexError: Stack is empty
 
'''
Queue: Implemented From a Linked List
The operations for a queue made from a linked list are the same as the operations for a queue made from an array.

The Code
'''
# FIFO Queue implementation using a linked list 
# as its underlying storage
class LinkedListQueue:
  # ----------------------Nested Node Class ----------------------
    # This Node class stores a piece of data (element) and
    # a reference to the Next node in the Linked List
    class Node:
        def __init__(self, e):
            self.element = e    
            self.next = None   # reference to the next Node

# ---------------------- queue methods -------------------------
    # create an empty queue
    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None

    # Add element e to the back of the queue.
    def enqueue(self, e):
        newest = self.Node(e)

        if self.is_empty():
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self._size += 1

    # Remove and return the first element from the queue
    # (i.e., FIFO). Raise exception if the queue is empty.
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')

        elementToReturn = self.head.element
        self.head = self.head.next
        self._size -= 1
        if self.is_empty():
            self.tail = None

        return elementToReturn

    # Return (but do not remove) the element at the front of
    # the queue. Raise exception if the queue is empty.
    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.head.element

    # Return True if the queue is empty.
    def is_empty(self):
        return self._size == 0

    # Return the number of elements in the queue.
    def size(self):
        return self._size


LLQ = LinkedListQueue()
LLQ.enqueue("L")
LLQ.enqueue("L")
LLQ.enqueue("Q")
LLQ.enqueue("U")
LLQ.enqueue("E")
LLQ.enqueue("U")
LLQ.enqueue("E")
LLQ.peek()         # L
LLQ.size()         # 7
LLQ.is_empty()     # False
LLQ.dequeue()      # L
LLQ.dequeue()      # L
LLQ.dequeue()      # Q
LLQ.dequeue()      # U
LLQ.dequeue()      # E
LLQ.dequeue()      # U
LLQ.dequeue()      # E
LLQ.is_empty()     # True
LLQ.size()         # 0
LLQ.peek()         # IndexError: Queue is empty
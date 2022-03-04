'''
Complexity Analysis:
Enqueue and Dequeue operations have complexity of O(1),
Applications:
1. CPU Scheduling
2. Memory Management
3. Traffic Management
'''

class CircularQueue:
    def __init__(self, size):
        self.size = size 
        self.queue = [None] * size 
        self.front = self.rear = -1

    def enqueue(self, val):
        if(self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = val
        elif((self.rear +1) % self.size == self.front):
            print("Queue Full.")
        else:
            print("Entered 3rd enqueue condition")
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = val 

    def dequeue(self):
        if(self.front == -1):
            print("Queue Empty.")
        elif(self.front == self.rear):
            temp = self.queue[self.rear]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front] 
            self.front += 1
            return temp 

    def print_queue(self):
        if(self.front == -1):
            print("Queue Empty")
        elif(self.rear >= self.front):
            i = self.front
            while(i <= self.rear):
                print(self.queue[i], end = " ")
                i += 1
            print()
        else:
            i = self.front
            while(i < self.size):
                print(self.queue[i], end = " ")
                i += 1
            i = self.rear
            while(i < self.front):
                print(self.queue[i], end = " ")
                i += 1
            print()

size = int(input("Enter size of circular queue : "))
if(size < 1):
    print("Circular queue can't exitst.")
else:
    queue = CircularQueue(size)
    while(True):
        ch = int(input("Enter 1 to enqueue, 2 to dequeue, 3 to display queueue, 4 to exit : "))
        if(ch == 1):
            val = int(input("Enter value : "))
            queue.enqueue(val)
        if(ch == 2):
            print("Dequeued element = ",queue.dequeue())
        if(ch == 3):
            queue.print_queue()
        if(ch == 4):
            break
                

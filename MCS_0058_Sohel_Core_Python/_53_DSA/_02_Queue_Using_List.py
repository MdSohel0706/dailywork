'''
Complexity Analysis:
Enqueue and Dequeue operations have complexity of O(1),
but if we dequeue by index then we may have a complexity of O(n).
Application:
1. Railway booking website.
2. CPU Scheduling.
3. Call centre call queues.
'''

class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, val):
        if(len(self.queue) < self.size):
            self.queue.append(val)
        else:
            print("Queue Full. Can't Enqueue.")

    def dequeue(self):
        if(len(self.queue) > 0):
            return self.queue.pop(0)
        else:
            print("Queue Empty.")

    def display(self):
        if(len(self.queue) > 0):
            print(self.queue)
        else:
            print("Queue Empty.")

    def size_q(self):
        if(len(self.queue) > 0):
            print("Queue Current Length : ",len(self.queue))
        else:
            print("Queue Empty.")

size = int(input("Enter the size of queue : "))

q = Queue(size)

while(True):
    ch = int(input("Enter 1 to enqueue, 2 to dequeue, 3 to display queueue, 4 to check current size, 5 to exit : "))
    if(ch == 1):
        val = int(input("Enter value : "))
        q.enqueue(val)
    if(ch == 2):
        print("Dequeued element = ",q.dequeue())
    if(ch == 3):
        q.display()
    if(ch == 4):
        q.size_q()
    if(ch == 5):
        break

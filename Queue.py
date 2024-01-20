class Queue:
    
    #FIFO
    
    def __init__(self):
        self.queue = []
        
    
    def enqueue(self,data):
        self.queue.append(data)
        
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty!!.")
        else:
            self.queue.pop(0)
    
    def display(self):
        print(self.queue)
            
q = Queue()
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)
q.display()
q.dequeue()
q.display()
    
        
#Another way

from queue import Queue
queue = Queue()
queue.put('a')  # enqueue 'a'
queue.put('b')  # enqueue 'b'
queue.put('c')  # enqueue 'c'
print(queue.get()) 
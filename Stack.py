class Stack:
    
    #LIFO
    
    def __init__(self):
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)  # push data onto the stack
    
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty!!.")
        else:
            self.stack.pop()  # pop off the top element
        
    def display(self):
        print(self.stack)

stack = Stack()
stack.push(10)
stack.push(9)
stack.display()
stack.pop()
stack.display()


#Another Way

from queue import LifoQueue
stack = LifoQueue()
stack.put('a')  # push 'a' onto the stack
stack.put('b')  # push 'b' onto the stack
stack.put('c')  # push 'c' onto the stack
print(stack.get())
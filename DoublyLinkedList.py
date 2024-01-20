class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None     


class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
        
    def inserAtLast(self, data):
        node = Node(data)
        
        if self.head is None:
            self.head = node
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            
            currentNode.next = node
            node.prev = currentNode
            
        self.size +=1
            
    def insertAtFirst(self, data):
        node = Node(data)
        
        if self.head is None:
            self.head= node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.size +=1
        
    def inserAtPosition(self, index, data):
        
        if index < 0 or index > self.size:
            print("Invalid index")
            return
        
        node = Node(data)
        
        if(index == 0 ):
            return self.insertAtFirst(data)
        elif (index == self.size):
            return self.inserAtLast(data)
        else:
            currentIndex = 0
            currentNode = self.head
        
            while currentIndex != index-1:
                currentNode = currentNode.next
            

            node.prev = currentNode
            node.next = currentNode.next
            currentNode.next.prev = node
            currentNode.next = node
        
        self.size +=1
        
        
    def removeLastNode(self):
        currentNode = self.head
        
        if(self.size == 1):
            self.head = None
        else:
            while currentNode.next.next is not None:
                currentNode = currentNode.next
        
            # currentNode.next.prev = None
            currentNode.next = None
        self.size -=1
    
    def removeFirstNode(self):
         if(self.size == 1):
            self.head = None
         else :
            self.head = self.head.next
            self.head.prev = None
         self.size -=1
    
    def removeParticularNode(self, data):
        
        if self.head is None:
            print("List is empty")
            return


        currentNode = self.head
        
        while currentNode is not None and currentNode.data != data:
            currentNode = currentNode.next
        
        if currentNode is None:  # data not found in list
            print("Node not found")
            return

        # remove node
        if currentNode.prev is not None:
            currentNode.prev.next = currentNode.next
        if currentNode.next is not None:
            currentNode.next.prev = currentNode.prev
            
        currentNode.prev = None
        currentNode.next = None

        self.size -= 1
            
        
    
    def display(self):
        # print(self.size)
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, end= " -> ")
            currentNode = currentNode.next
        
dd = DoublyLinkedList()

dd.insertAtFirst(10)
dd.insertAtFirst(9)
dd.insertAtFirst(8)
dd.insertAtFirst(7)
dd.insertAtFirst(6)
dd.inserAtLast(11)

dd.display()     
print()
# dd.inserAtPosition(1,5)
dd.removeParticularNode(7)
dd.display()
            
            
            
        
        
        
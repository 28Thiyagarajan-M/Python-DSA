class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def insertAtFirst(self, data):
        node = Node(data)
        if self.head is None: 
            self.head = node
        else :
            node.next = self.head
            self.head = node
        self.size += 1
        
    def insertAtLast(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next 
            currentNode.next = node
        self.size += 1
            
    def removeLastNode(self):
        if self.head is None:
            print("Linked List is Empty!!.")
        elif self.head.next is None:
            self.head = None
        else:
            currentNode = self.head
            while currentNode.next.next is not None:
                currentNode = currentNode.next
            currentNode.next = None
        self.size -= 1
    
    def removeFirstNode(self):
        if self.head is None:
            print("Linked List is Empty!!.")
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.size -= 1
        
    def findTheMiddleNode(self):
        pointer_1 = self.head
        pointer_2 = self.head

        while pointer_2 is not None and pointer_2.next is not None:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next.next

        print(f"Middle Node is :  {pointer_1.data}")
        
    def insertAtPosition(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Invalid index")

        node = Node(data)

        if index == 0:
            self.insertAtFirst(data)
        elif index == self.size:
            self.insertAtLast(data)
        else:
            currentNode = self.head
            currentIndex = 0

            while currentIndex != index - 1:
                currentNode = currentNode.next
                currentIndex += 1

            node.next = currentNode.next
            currentNode.next = node

        self.size += 1

    def removeParticularNode(self, data):
        if self.head is None:
            raise ValueError("Linked List is Empty!!.")

        if self.head.data == data:  # data found in head node
            self.removeFirstNode()
        else:
            currentNode = self.head
            while currentNode.next is not None and currentNode.next.data != data:
                currentNode = currentNode.next

            if currentNode.next is None:  # data not found in list
                raise ValueError("Node not found")
            else:  # data found
                temp = currentNode.next
                currentNode.next = currentNode.next.next
                temp.next = None

        self.size -= 1

    def display(self):
        currentNode = self.head
        print("LinkedList : ")
        while currentNode is not None:
            print(currentNode.data, end=" ")
            currentNode = currentNode.next
        print(f"\nSize :{self.size}")

ll = LinkedList()
ll.insertAtFirst(10)
ll.insertAtFirst(9)
ll.removeFirstNode()
ll.insertAtFirst(8)
ll.insertAtFirst(7)
ll.removeLastNode()
ll.insertAtFirst(6)
ll.insertAtLast(11)

ll.display()

ll.findTheMiddleNode()


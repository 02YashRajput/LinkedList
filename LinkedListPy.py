class Node:

    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

        
class LinkedList:

    def __init__(self):
        self.head = None
    
    def insertAtBegin(self,data):
        newNode = Node(data,self.head)
        self.head = newNode


    def insertAtEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while(currentNode.next):
                currentNode = currentNode.next
            currentNode.next = newNode

    def insertAtIndex(self,data,index):
        newNode = Node(data)
         
        if index ==0:
           self.insertAtBegin(data)
        elif index <0:
            return
        else:
            currentNode = self.head
            while(index !=1 and currentNode!=None):
                currentNode = currentNode.next
                index -=1
            if currentNode!=None:
                newNode.next = currentNode.next
                currentNode.next = newNode
            else:
                print("index not found")

    def deleteAtBegin(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next

    def deleteAtEnd(self):
        if self.head is None:
            return
        else:
            currentNode = self.head
            if currentNode.next is None:
                self.head = None
            else:
                while(currentNode.next.next):
                    currentNode = currentNode.next
                currentNode.next = None

    def deleteAtIndex(self,index):
        if index == 0:
            self.head = self.head.next
        elif index < 0:
            return
        
        else:
            currentNode = self.head
            while(index !=1 and currentNode!=None):
                currentNode = currentNode.next
                index -=1
            if currentNode!=None:
                currentNode.next = currentNode.next.next
            else:
                print("index not found")

    def update(self,data,index):
        if index ==0:
           self.head.data = data
        elif self.head is None or index <0:
            return
        else:
            currentNode = self.head
            while(index !=0 and currentNode!=None):
                currentNode = currentNode.next
                index -=0
            if(currentNode!=None):
                currentNode.data = data
            else:
                print("index not found")
                
    def display(self):
        if(self.head):
            currentNode = self.head
            while(currentNode):
                print(currentNode.data)
                currentNode = currentNode.next
        else:
            print("Linked List is empty")
    
    def reverse(self):
        if self.head is None:
            print("Linked List is empty")
            return
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def size(self):
        size = 0
        if self.head :
            currentNode = self.head
            while(currentNode):
                currentNode = currentNode.next
                size+=1
        print(f"Size of LinkedList is {size}")


L1 = LinkedList()
L1.insertAtEnd(1)
L1.insertAtEnd(2)
L1.insertAtEnd(4)
L1.insertAtEnd(4)
L1.insertAtEnd(5)
L1.insertAtBegin(0)
L1.insertAtIndex(3,3)
L1.display()
print()
L1.deleteAtBegin()
L1.deleteAtEnd()
L1.deleteAtIndex(4)
L1.display()
print()
L1.size()

L2 = LinkedList()
L2.display()
L2.size()


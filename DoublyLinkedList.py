class Node:
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    
class DoublyLinkedList:

    def __init__(self):
        self.head = None
        
    
    def insertAtBegin(self,data):
        newNode = Node(data,self.head)
        if self.head:
            self.head.prev = newNode
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
            newNode.prev = currentNode

    def insertAtIndex(self,data,index):
        newNode = Node(data)
        if index == 0:
            self.insertAtBegin(data)
        elif index<0:
            return  
        else:
            currentNode = self.head
            while(index != 1 and currentNode!=None):
                currentNode = currentNode.next
                index-=1
            if(currentNode!=None and currentNode.next!= None):
                
                newNode.next = currentNode.next
                currentNode.next.prev = newNode
                currentNode.next = newNode
                newNode.prev = currentNode
            elif(currentNode.next == None):
                newNode.prev = currentNode
                currentNode.next = newNode
            else:
                print("index not found")


    def deleteAtBegin(self):
        if(self.head):
            self.head.next.prev = None
            self.head = self.head.next
        else:
            print("Empty Linked list")


    def deleteAtEnd(self):
        if(self.head):
            currentNode = self.head
            while(currentNode.next.next):
                currentNode = currentNode.next
            currentNode.next = None
        else:
            print("Empty Linked list")

    def deleteAtIndex(self,index):
        if self.head is None:
            print("Empty Linked list")
            return
        elif(index == 0):
            self.head.next.prev = None
            self.head.next = self.head
        else:
            currentNode = self.head
            while(index !=1 and currentNode != None):
                currentNode = currentNode.next
                index-=1
            if(currentNode!=None and currentNode.next.next!=None):
                currentNode.next.next.prev = currentNode
                currentNode.next = currentNode.next.next
            elif(currentNode!=None and currentNode.next.next==None):
                currentNode.next = None
            else:
                print("index not found")


    def display(self):
        if(self.head):
            currentNode = self.head
            while(currentNode):
                print(currentNode.data)
                currentNode = currentNode.next
        else:
            print("Empty Linked list")


L1 = DoublyLinkedList()
L1.insertAtEnd(1)
L1.insertAtEnd(2)
L1.insertAtBegin(0)
L1.display()
L1.insertAtIndex(3,3)
print()
L1.display()


    

        

        
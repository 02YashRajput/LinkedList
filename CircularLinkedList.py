class Node:

    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class CircularLinkedList:

    def __init__(self):
        self.head = None


    def insertAtBegin(self,data):
        if self.head is None:
            newNode = Node(data,newNode)
            self.head = newNode
        else:
            newNode = Node(data,self.head)
            currentNode = self.head
            while currentNode.next!=self.head:
                currentNode = currentNode.next
            currentNode.next = newNode
            self.head = newNode


    def insertAtEnd(self,data):
        if self.head is None:
            newNode = Node(data,newNode)
            self.head = newNode
        else:
            newNode = Node(data,self.head)
            currentNode = self.head
            while currentNode.next!=self.head:
                currentNode = currentNode.next
            currentNode.next = newNode
             

    def insertAtIndex(self,data,index):
        if self.head is None:
            print("Empty LinkedList")
        elif(index == 0):
            self.insertAtBegin(data)
        else:
            currentNode = self.head
            newNode = Node(data)
            while(currentNode!=None and index!=1):
                currentNode = currentNode.next
                index -=1
            if(currentNode!=None):
                newNode.next = currentNode.next
                currentNode.next = newNode
            else:
                print("index not found")



            
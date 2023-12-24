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
        if(index == 0):
            self.insertAtBegin(data)
        elif index<0:
            print("Enter valid index")
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


    def delete_at_beginning(self):
        if not self.head:
            print("Empty Circular Linked List")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print("Empty Circular Linked List")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
            temp.next = self.head

    def delete_at_index(self, index):
        if not self.head:
            print("Empty Circular Linked List")
            return

        if index == 0:
            self.delete_at_beginning()
        else:
            currentNode = self.head
            while(index !=1 and currentNode!=None):
                currentNode = currentNode.next
                index -=1
            if currentNode!=None:
                currentNode.next = currentNode.next.next
            else:
                print("index not found")

    def display(self):
        if self.head:
            currentNode = self.head.next
            print(self.head.data)
            while(currentNode!=self.head):
                print(currentNode.data)
                currentNode = currentNode.next
        else:
            print("list is empty")


        
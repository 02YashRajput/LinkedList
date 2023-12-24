class Node:
    def __init__(self,row,col,data,next=None):
        self.row = row
        self.col = col
        self.data = data
        self.next = next


class SparseMatrix:
    def __init__(self):
        self.head = None

    def createNewNode(self,row,col,data):
        newNode = Node(row,col,data)
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while(currentNode.next):
                currentNode = currentNode.next
            currentNode.next = newNode
    

    def display(self):
        temp = self.head
        print("Row  Column  Value")
        while temp != None:
            print(temp.row, "    ", temp.col ,"     ", temp.data)
            temp = temp.next    


S = SparseMatrix()
sparseMatric = [[0, 0, 3, 0, 4],
                    [0, 0, 5, 7, 0],
                    [0, 0, 0, 0, 0],
                    [0, 2, 6, 0, 0]]

for i in range(4):
    for j in range(5):
        if sparseMatric[i][j] !=0:
            S.createNewNode(i, j, sparseMatric[i][j])

S.display()




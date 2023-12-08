class Node:
    def __init__(self,val,pow,next = None):
        self.val = val
        self.pow = pow
        self.next = next


class Polynomial:
    def __init__(self):
        self.head = None

    
    def createPolynomial(self,val,pow):
        newNode = Node(val,pow,self.head)
        self.head = newNode

            





class Node:
    def __init__(self):
        self.data =data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head = None
    def insertHead(self,Newnode):
        tempNode= self.head
        self.head = Newnode
        self.head.next = tempNode
        del tempNode
    
    def insertAt(self,Newnode,position):
        if position < 0 or position > self.listLength()

#from LinkedList import Node, LinkedList
from LinkedList import Node

class CDLL:
    def __init__(self, data=None):
        self.head = Node(data)
        self.head.next = self.head
        self.head.prev = self.head
        print("New Circular Doubly Linked list created.")
        
    
    def IsEmpty():
        if self.head == None:
            return True
        else: return False

    def InsertAtEnd(self, data):
        if self.head == None:
            print("EMpty linked list.")
        else:
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            new = Node(data, next=self.head,prev=ptr)
            ptr.next = new
            self.head.prev = new
            
                    
    def InsertAtBeginning(self, data):
        if self.head == None:
            print("EMpty linked list.")
        else:
            new = Node(data)
            ptr = self.head
            while ptr.next != self.head:
                ptr=ptr.next
            ptr.next = new
            new.prev = ptr
            new.next = self.head
            self.head.prev = new
            self.head = new
            

    
    def InsertAfter():
        print("Implementation of this function in subclass is pending.!")
    
    def InsertBefore():
        print("Implementation of this function in subclass is pending.!")
    
    
    def DeleteAtEnd(self):
        if self.head == None:
            print("Empty Linked List")
        else:
            ptr = self.head
            while ptr.next != self.head:
                preptr = ptr
                ptr = ptr.next
            preptr.next = self.head
            self.head.prev = preptr
            del ptr
   
    
    def DeleteAtBeginning(self):
        if self.head == None:
            print("Empty LinkedList")
        else:
            preptr = ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            self.head = self.head.next
            self.head.prev = ptr
            ptr.next = self.head
            del preptr
    
    
    def DeleteAfter():
        print("Implementation of this function in subclass is pending.!")
    
    
    def DeleteBefore():
        print("Implementation of this function in subclass is pending.!")


    def DeleteLL(self):
        ptr = self.head
        while ptr.next != self.head:
            preptr = ptr
            ptr = ptr.next
            del preptr
        del ptr
        print("successfully deleted!!")
    
    def DisplayLL(self):
        ptr = self.head
        print("Head <-> ", end="")
        while ptr.next != self.head:
            print(ptr.data, " <--> ", end="", sep="")
            ptr = ptr.next
        print(ptr.data, " <-> Head", sep="",)
    

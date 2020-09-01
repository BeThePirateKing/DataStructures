#from LinkedList import Node, LinkedList
from LinkedList import Node
class SLL:

    def __init__(self, data=None):
        self.head = Node(data)
        print("New Singly Linked list created.")
        
    
    def IsEmpty():
        if self.head == None:
            return True
        else: return False

    def InsertAtEnd(self, data):
        if self.head == None:
            print("EMpty linked list.")
        else:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = Node(data)
                    
    def InsertAtBeginning(self, data):
        if self.head == None:
            print("EMpty linked list.")
        else:
            new = Node(data)
            new.next = self.head
            self.head = new
    
    def InsertAfter(self):
        print("Implementation of this function in subclass is pending.!")
    
    def InsertBefore(self):
        print("Implementation of this function in subclass is pending.!")
    
    
    def DeleteAtEnd(self):
        if self.head == None:
            print("Empty Linked List")
        else:
            ptr = self.head
            while ptr.next != None:
                preptr = ptr
                ptr = ptr.next
            preptr.next = None
            del ptr
   
    
    def DeleteAtBeginning(self):
        if self.head == None:
            print("Empty LinkedList")
        else:
            preptr = self.head
            self.head = self.head.next
            del preptr
    
    
    def DeleteAfter(self):
        print("Implementation of this function in subclass is pending.!")
    
    
    def DeleteBefore(self):
        print("Implementation of this function in subclass is pending.!")

    def DeleteLL(self):
        ptr = self.head
        while ptr.next != None:
            preptr = ptr
            ptr = ptr.next
            del preptr
        del ptr
        print("successfully deleted!!")
    
    def DisplayLL(self):
        ptr = self.head
        print("Head->", end="")
        while ptr.next != None:
            print(ptr.data, "->", end="", sep="")
            ptr = ptr.next
        print(ptr.data, "->X", sep="")
    

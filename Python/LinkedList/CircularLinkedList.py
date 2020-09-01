from LinkedList import Node

class CLL:
    
    def __init__(self, data=None):
        self.head = Node(data)
        self.head.next = self.head
        print("New Circular Linked List created.")
        
    
    def IsEmpty():
        if self.head == None:
            return True
        else: return False

    def InsertAtEnd(self, data):
        if self.head == None:
            print("Empty linked list.")
        else:
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            new = Node(data)
            ptr.next = new
            new.next = self.head
                    
    def InsertAtBeginning(self, data):
        if self.head == None:
            print("EMpty linked list.")
        else:
            new = Node(data)
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = new
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
            while ptr.next != self.head:
                preptr = ptr
                ptr = ptr.next
            preptr.next = self.head
            del ptr
   
    
    def DeleteAtBeginning(self):
        if self.head == None:
            print("Empty LinkedList")
        else:
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = self.head.next
            self.head = self.head.next
            del ptr
    
    
    def DeleteAfter(self):
        print("Implementation of this function in subclass is pending.!")
    
    
    def DeleteBefore(self):
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
        print("Head->", end="")
        while ptr.next != self.head:
            print(ptr.data, "->", sep="", end="")
            ptr = ptr.next
        print(ptr.data, "->Head", sep="")
    
from abc import ABC, abstractmethod
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def getData(self):
        return self.data
"""
class LinkedList(ABC, abstractmethod):
    @abstractmethod
    def InsertAtEnd():
        print("Implementation of this function is pending.!")
    
    @abstractmethod
    def InsertAtBeginning():
        print("Implementation of this function is pending.!")
    
    @abstractmethod
    def InsertAfter():
        print("Implementation of this function is pending.!")
    
    @abstractmethod
    def InsertBefore():
        print("Implementation of this function is pending.!")
    
    @abstractmethod
    def DeleteAtEnd():
        print("Implementation of this function is pending.!")
    
    @abstractmethod
    def DeleteAtBeginning():
        print("Implementation of this function is pending.!")
    
    @abstractmethod
    def DeleteAfter():
        print("Implementation of this function is pending.!")
    
    @abstractmethod
    def DeleteBefore():
        print("Implementation of this function is pending.!")
    
    @abstractmethod
    def DeleteLL(self):
        print("Implementation of this function is pending.!")
    
    @abstractmethod
    def DisplayLL(self):
        print("Implementation of this function is pending.!")
    
"""
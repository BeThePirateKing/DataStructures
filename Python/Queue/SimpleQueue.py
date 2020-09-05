from LinkedList.LinkedList import Node

class SimpleQueue:

    def __init__(self, data):
        print("New Simple Queue created.")
        self.head = Node(data)
        self.front = self.head
        self.rear = self.head
        self.noOfElements = 1
    
    def Enqueue(self, data):
        self.noOfElements += 1
        new = Node(data)
        self.rear.next = new
        self.rear = new

    
    def Dequeue(self):
        self.noOfElements -= 1
        ptr = self.head
        self.head = self.head.next
        self.front = self.head
        return ptr        

    def Display(self):
        print("FP,Head->", end="")
        ptr = self.front
        while ptr != self.rear:
            print(ptr.data, "<-", end="", sep="")
            ptr=ptr.next
        print(self.rear.data, "<-RP", sep="")
        pass

    def getNoOfElements(self):
        return self.noOfElements

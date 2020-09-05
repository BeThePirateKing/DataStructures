class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CBT:
    count = 0
    def __init__(self,data):
        if count == 0:
            self.head = Node(self)
            self.root = self
        count += 1
        self.data = data
        self.left = None
        self.right = None

    def getData(self):
        return self.data
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right

    def setLeft(self, new):
        self.left = new

    def setRight(self, new):
        self.right = new

    def addToList(self, new):
        ptr = self.head
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = Node(new)

    #return the empty location in tree
    def getEmptyLocation(self):
        ptr = self.head
        while ptr.next != None:
            node = ptr.data
            if node.getLeft() == None:
                return node.getLeft()
            elif node.getRight() == None:
                return node.getRight()
            else:
                pass
            ptr = ptr.next

    #insert the element
    def insert(self, data):
        new = CBT(data)
        node = self.getEmptyLocation()
        node = new
        self.addToList(new)

    #deletes the element if found 
    def delete(self, data):
        #delete in tree
        pass
        #delete in list

    #search for the given element
    def search(self, data):
        pass
    
    #return height of enitre tree given leaf nodes at height zero
    def height(self):
        pass

    #pre-order-traversal
    def getPreOT(self):
        pass
    #in-order-traversal
    def getInOT(self):
        pass
    
    #post-order-traversal
    def getPostOT(self):
        pass

    #returns leaf nodes
    def getLeaves(self):
        pass

    #returns number of internal nodes
    def getInternalNodes(self):
        pass
    
    #returns total nodes in tree
    def getTotalNodes(self):
        return count

    

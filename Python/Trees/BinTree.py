
class BinaryTree:
    count = 0
    def __init__(self,data):
        if count == 0:
            self.root = self
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

    #insert the element
    def insert(self, data):
        pass
    
    #deletes the element if found 
    def delete(self, data):
        pass
    
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
    def getNumberOfLeaves(self):
        pass

    #returns number of internal nodes
    def getInternalNodes(self):
        pass
    
    #returns total nodes in tree
    def getTotalNodes(self):
        return count

    

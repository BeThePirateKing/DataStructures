class BST:
    count = 0
    root = None
    def __init__(self,data):
        if count == 0:
            root = self
            self.height = 0
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        
        count += 1

    def setParent(self, new):
        self.parent = new
    
    def getParent(self):
        return self.parent

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

    def isRoot(self):
        return self == root

    def setRoot(self, root):
        root = root

    def getRoot(self):
        return root

    def isLeaf(self):
        return self.getLeft() == None and self.getRight() == None

    def isLeftChild(self):
        return self.getParent().getLeft() == self

    def isRightChild(self):
        return self.getParent().getRight() == self

    def getLocation(self, data):
        node = self
        if node.getData() > data:
            if node.getLeft() == None:
                return node
            else:
                return node.getLeft().getLocation(data)
        else:
            if node.getRight() == None:
                return node
            else:
                return node.getRight().getLocation(data)

    def getLargestSuccessor(self):
        if self.getRight():
            return self.getRight().getLargestSuccessor()
        else:
            return self
    
    def getSmallestPredecessor(self):
        if self.getLeft():
            return self.getLeft.getSmallestPredecessor()
        else:
            return self

    def SwapWith(self, other):
        other.setLeft(self.getLeft())
        other.setRight(self.getRight())
        other.setParent(self.getParent())  

    def setChildToNone(self):
        if self.isLeftChild():
            self.getParent().setLeft(None)
        else:
            self.getParent().setRight(None)

    def insert(self, data):
        node = self.getLocation(data)
        new = BST(data)
        if node.getLeft() == None:
            node.setLeft(new)
            new.setParent(node)
        else:
            node.setRight(new)
            new.setParent(node)
        
        

    #deletes the element if found 
    def delete(self, data):
        #delete in tree
        node = self.root.search(data)
        if node:
            if node.isLeaf():
                node.setChildToNone()
                del node
            else:
                successor = node.getLargestSuccessor()
                if successor:
                    if successor.isLeaf():
                        node.SwapWith(successor)
                        if node.isRoot():
                            node.setRoot(successor)
                        del node
                    else:
                        successor.getParent().setRight(successor.getLeft())
                        node.SwapWith(successor)
                        if node.isRoot():
                            node.setRoot(successor)
                        del node
                else:
                    predecessor = node.getSmallestPredecessor()
                    if predecessor.isLeaf():
                        node.SwapWith(predecessor)
                        if node.isRoot():
                            node.setRoot(predecessor)
                        del node
                    else:
                        predecessor.getParent().setLeft(predecessor.getRight())
                        node.SwapWith(predecessor)
                        if node.isRoot():
                            node.setRoot(predecessor)
                        del node
        else:
            print("No such node exist.")
        
        

    #search for the given element
    def search(self, data):
        try:
            if self.getData() > data:
                return self.getLeft().search(data)
            elif self.getData() < data:
                return self.getRight().search(data)
            elif self.getData() == data:
                return self
        except TypeError:
            return 0

    #return height of enitre tree given leaf nodes at height zero
    def getHeight(self):
        if self.isLeaf():
            self.height = 0
            return self.height
        else:
            if self.getLeft == None:
                self.height = 1 + self.getRight().getHeight() 
                return self.height
            elif self.getRight() == None:
                self.height = 1 +  self.getLeft().getHeight()
                return self.height
            else:
                self.height = 1 + max(self.getLeft().getHeight(), self.getRight().getHeight()) 
                return self.height

    #pre-order-traversal
    def getPreOrder(self):
        print(self.getData())
        if self.getLeft() and self.getRight():
            self.getLeft().getPreOrder()
            self.getRight().getPreOrder()
            return
        elif self.getLeft() == None:
            self.getRight().getPreOrder()
            return
        elif self.getRight() == None:
            self.getLeft.getPreOrder()
            return
        else:
            return

        
    #in-order-traversal
    def getInOrder(self):
        if self.getLeft() and self.getRight():
            self.getLeft().getInOrder()
            print(self.data)
            self.getRight().getInOrder()
            return
        elif self.getLeft() == None and self.getRight() == None:
            print(self.data)
            return
        elif self.getLeft() == None:
            print(self.data)
            self.getRight().getInOrder()
            return
        elif self.getRight() == None:
            self.getLeft().getInOrder()
            print(self.data)
            return
        else:
            return
        
    #post-order-traversal
    def getPostOrder(self):
        


    #returns total nodes in tree
    def getTotalNodes(self):
        return count
    




from BST import BST

class AVL(BST):

    def __init__(self,data):
        super.__init__(self,data)

    def getHeight(self):
        pass

    def getBalanceFactor(self):
        return self.getLeft().getHeight() - self.getRight().getHeight()

    def insert(self, data):
        node = self.getLocation(data)
        new = AVL(data)
        if node.getLeft() == None:
            new.setParent(node)
            node.setLeft(new)
        else:
            new.setParent(node)
            node.setRight(new)
        self.root.Balance()

    def delete(self, data):
        super.delete(self, data)
        self.getRoot().Balance()

    def RightRotate(self):
        left = self.getleft()
        left.setParent(self.getParent())
        self.getParent().setLeft(left)
        self.setLeft(left.getRight())
        self.setParent(left)
        left.setRight(self)


    def LeftRotate(self):
        right = self.getRight()
        right.setParent(self.getParent())
        self.getParent().setRight(right)
        self.setright(right.getLeft())
        self.setParent(right)
        right.setLeft(self)


    def Balance(self):
        if self.getBalanceFactor() == 2:
            #Then left subtree is greater then right one
            left = self.getLeft()
            right = self.geetRight()
            if left.getBalanceFactor() == 0:
                #R0-deletion
                self.RightRotate()
            elif right.getBalanceFactor() == 0:
                #RO-deletion
                self.LeftRotate()

            elif left.getBalanceFactor() == 1:
                #LL
                self.RightRotate()
            elif right.getBalanceFactor() == 1:
                #R1-deletion
                self.LeftRotate()
            elif left.getBalanceFactor() == -1:
                #LR
                left.LeftRotate()
                self.RightRotate()
            elif right.getBalanceFactor() == -1:
                #R-1 Rotation
                right.RightRotate()
                self.LeftRotate()
            else:
                left.Balance()

        elif self.getBalanceFactor() == -2:
            #Then right subtree is greater than left one
            left = self.getLeft()
            right = self.getRight()
            if left.getBalanceFactor() == 0:
                #R0 rotation
                self.RightRotate()
            elif right.getBalanceFactor() == 0:
                #R0 rotaion
                self.LeftRotate()
            elif right.getBalanceFactor() == -1:
                #RR
                self.LeftRotate()
            elif left.getBalanceFactor() == -1:
                self.RightRotate()

            elif right.getBalanceFactor() == 1:
                #RL
                right.RightRotate()
                self.LeftRotate()
            elif left.getBalanceFactor() == 1:
                left.LeftRotate()
                self.RightRotate()
            else:
                right.Balance()
            pass
        else: return





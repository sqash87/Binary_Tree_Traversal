#Creating a binary tree

from itertools import tee
from logging import NullHandler


class BinaryTree:

    #This function will create the tree
    def __init__(self, key):
        self.right= None
        self.left = None
        self.data = key
   
     # Preorder Traversal
    def Traverse(self):
        
        print( self.data, end=' ')
       
        # if the next node is not null, call the Traverse functio again
        if self.left:
            self.left.Traverse()
        #if the next nonde is not null, call the traverse function
        if self.right:
            self.right.Traverse()
    
    # Postorder Travsersal: 
        #1. Visit all the left nodes
        #2. Visit all the right nodes.
        #3. vist the node.
    def PostTraverse(self):
        if self.left:
            self.left.PostTraverse()
        
        if self.right:
             self.right.PostTraverse()
        print(self.data, end= ' ')
        
    
    #Inorder travsersal:
        #1: visit all the nodes in the left subtree
        #2: Then the root node
        #3: Visit all the nodes in the right subtree

    def InorderTraverse(self):
        if self.left:
            self.left.InorderTraverse()
        
        print(self.data, end= ' ')
        
        if self.right:
            self.right.InorderTraverse()


tree = BinaryTree(10) # creates the root node
tree.left = BinaryTree(12)
tree.right =BinaryTree(13)
tree.left.left = BinaryTree(15)
tree.left.right = BinaryTree(16)
tree.left.left.right= BinaryTree(33)
tree.right.right =BinaryTree(17)
tree.right.right.left = BinaryTree(21)
tree.right.right.right = BinaryTree(25)

print("\n")

print("Posorder Traversal:", end= ' ')
tree.PostTraverse()
print("\n")

print("Preorder travsersal:", end = ' ')
tree.Traverse()
print("\n")

print("Inreorder travsersal:", end = '')
tree.InorderTraverse()
print("\n")






    

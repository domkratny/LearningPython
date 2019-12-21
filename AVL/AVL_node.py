# -*- coding: utf-8 -*-
"""
Created on Dec 20, 2019

@author: Vlad for SY and Ben
"""
## ==========================================================
class AVLNode:
    def __init__(self):
        self.parent = None
        self.left   = None
        self.right  = None
        self.data   = None
    
    def push(self, num):
        return self
            
        
    def delete(self, num):
        pass
        

    def printTree(self, i = 1, pre = ""):
        if self.data is None:
            return
        
        self.printTree(self.left, pre)
        print(pre + str(self.data))
        self.printTree(self.right, pre)
        
if __name__ == "__main__":
    x = [ a for a in range(13)]
    random.shuffle(x)
    print(x)
    
    root = AVLNode()
    for a in x:
        root = root.push(a)
               
    root.printTree()
 
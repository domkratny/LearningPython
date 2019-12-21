# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:04:02 2019

@author: Vlad for SY and Ben
"""
import random

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

## ==========================================================
## to find paret/left/right nodes we are using one-base index
## then adjust to zero-base to locate element in array
 
class PriorityQueue:
    def __init__(self):
        self.arr = []
    
    def push(self, num):
        self.arr.append(num)
        n = len(self.arr)
        iparent = (n >> 1)
        while iparent > 0 and self.arr[n-1] < self.arr[iparent-1]:
            swap(self.arr, n-1, iparent-1 )
            n = iparent
            iparent = (n >> 1)
            
        
    def pop(self):
        temp = self.arr[0]
        self.arr[0] = self.arr[-1] 
        del self.arr[-1]
        iparent = 1
        while iparent < len(self.arr): 
            left = iparent << 1
            right = left + 1
            if right > len(self.arr) and left > len(self.arr):
                break
            elif right > len(self.arr):
                if self.arr[left-1] < self.arr[iparent-1]:
                    swap(self.arr, left  - 1, iparent - 1)
                    iparent = left
                else:
                    break
            else: 
                if self.arr[left-1] < self.arr[right-1] and self.arr[left-1] < self.arr[iparent-1]:
                    swap(self.arr, left  - 1, iparent - 1)
                    iparent = left
                elif self.arr[left-1] > self.arr[right-1] and self.arr[right-1] < self.arr[iparent-1]:
                    swap(self.arr, right - 1, iparent - 1)
                    iparent = right
                else:
                    break
                    
        return temp
        

    def printTree(self, i = 1, pre = ""):
        if i > len(self.arr):
            return
        
        left  = i << 1
        right = left + 1
        pre = pre + " - "
        self.printTree(left, pre)
        print(pre + str(self.arr[i-1]))
        self.printTree(right, pre)
        
if __name__ == "__main__":
    x = [ a for a in range(13)]
    random.shuffle(x)
    print(x)
    
    l1 = PriorityQueue()
    for a in x:
        l1.push(a)
        
    print("== printing priority queue (internal array) ==> \n" +str(l1.arr))
    print("== printing priority queue as a tree ==> ")
        
    l1.printTree()
    
    print("===========")
    
    while len(l1.arr):
        elm = l1.pop()
        print(elm)

    
    
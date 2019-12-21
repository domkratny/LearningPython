# -*- coding: utf-8 -*-
"""
Created on Sat Nov  22 

@author: Vlad for SY and Ben
"""
import random

class DNode:
    def __init__(self, data):
        # constructor class
        # store data and pointer to the next object
        self.data = data
        self.next = None
        self.prev = None
        return
    

class DList:
    def __init__(self):
        # constructor class
        # store head and tail of linked list
        self.head = None
        self.tail = None
        return
     
    def push_back(self, data):
        if self.tail is None:
            self.tail = DNode(data)
            self.head = self.tail
        else:
            temp = self.tail
            self.tail = DNode(data)
            temp.next = self.tail
            self.tail.prev = temp
                
    def push_front(self, data):
        if self.tail is None:
            self.tail = DNode(data)
            self.head = self.tail
        else:
            temp = self.head
            self.head = DNode(data)
            temp.prev = self.head
            self.head.next = temp
    
    def pop_back(self):
        if self.head is not self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.tail = None
            self.head = None
        
    def pop_front(self):
        if self.head is not self.tail:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.tail = None
            self.head = None
        
    def split(self):
        if self.head is None or self.head.next is None:
            return None
        
        slow = self.head.next
        fast = self.head.next.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        ret_list = DList()
        ret_list.head = slow
        ret_list.tail = self.tail
        self.tail = slow.prev
        slow.prev.next = None
        ret_list.head.prev = None
        return ret_list 
        
    def merge(self, L2):
        if L2.head is None:
            return self
        
        if self.head is None:
            self.head = L2.head
            self.tail = L2.tail
            return self
        
        curr = self.head
        while curr is not None and L2.head is not None:
            if curr.data > L2.head.data:
                temp = L2.head
                L2.pop_front()
                if curr.prev is None:
                    temp.next = curr
                    curr.prev = temp
                    self.head = temp
                else:
                    temp2 = curr.prev
                    curr.prev  = temp
                    temp2.next = temp
                    temp.next  = curr
                    temp.prev  = temp2
            else:
                curr = curr.next
                
        if L2.head is not None:
            self.tail.next = L2.head
            L2.head.prev = self.tail
            self.tail = L2.tail                   
        
            
            
    def print(self, forward = True):
        if self.head is None:
            print("Linked List is empty")
            return
        if forward:
            current_node = self.head
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next 
        else:
            current_node = self.tail
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.prev 


def mergeSort(l1):
    l2 = l1.split()
    if l2 is None:
        return l1
    l1 = mergeSort(l1)
    l2 = mergeSort(l2)
    l2.merge(l1)
    return l2

                
if __name__ == "__main__":
    l1 = DList()
    x = [ a for a in range(11)]
    random.shuffle(x)
    
    for a in x:
        l1.push_back(a)
    l1.print()
    
    
    l2 = mergeSort(l1)
    print("after merge")
    l2.print()
    


#!/usr/bin/python3

'''
In this class, we learn about Linear Linked Lists and implementation in Python.

Highlights:
    - Analyze the problem and create a pseudocode on how you will solve it
    - 
'''

from typing import Any

class Node:
    '''Implementing a linked list

    Args:
        data (Any): the data to be added to the head of the node.
    
    Return:
        Nothing

    Usage:
    node1 = Node(10)
    # Will add 10 to the head of the node
    '''
    def __init__(self, data):
        self.head = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBeg(self, data):
        self.head = data

    def printList(self):
        if not self.head:
            print("The linkedlist is empty.")
        
        else:
            current = Node
            while current:
                print(f"{current}->", end="")
                current 
#!/usr/bin/python3

class Node():
    def __init__(self, data):
        self.head = data
        self.next = None
    
def insert_at_beginning(data):
    # Initiate new Node
    new_node = Node(data)
    # Check for 
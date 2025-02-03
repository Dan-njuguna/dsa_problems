class Node():
    def __init__(self, data):
        self.head = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node
    def printLinkedList(self):
        current = self.head
        while current:
            if current.next is None:
                print(f"{current.head}")
            else:
                print(current.head, end=" -> ")
            
            current = current.next

        print()
    
    def insertEnd(self, data):
        self.data = data
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        
        else:
            current = self.head
            while current:
                current = current.next
            
            current.next = newNode
        

linked_list = LinkedList()
linked_list.insert_node("A")
linked_list.insert_node("B")
linked_list.insert_node("C")
linked_list.insertEnd("Wag")
linked_list.printLinkedList()

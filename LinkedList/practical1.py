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
    def printLinkedList(head):
        current = head
        while current:
            print(current.head, end=" -> ")
            current = current.next

        print()
        print("None")

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = linked_list.insert_node(1)
    linked_list.insert_node(2)
    linked_list.insert_node(3)
    linked_list.printLinkedList()
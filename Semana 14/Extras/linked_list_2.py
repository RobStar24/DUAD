class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, data):
        if self.head is None:
            print("Empty List")
            return
        
        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        
        prev = self.head
        current = self.head.next

        while current:
            if current.data == data:
                prev.next = current.next
                if current.next is None:
                    self.tail = prev
                return
            prev = current
            current = current.next

    def print_all(self):
        if self.head is None:
            print("Empty List")
            return
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")


ll = LinkedList()
ll.insert_front(10)
ll.insert_front(20)
ll.print_all()  # Prints: 20 -> 10 -> None

ll.insert_back(30)
ll.print_all()  # Prints: 20 -> 10 -> 30 -> None

ll.delete(10)
ll.print_all()  # Prints: 20 -> 30 -> None

ll.delete(20)
ll.print_all()  # Prints: 30 -> None

ll.delete(30)
ll.print_all()  # Prints: Empty List

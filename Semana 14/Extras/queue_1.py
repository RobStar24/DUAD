class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return "Queue is empty"
        removed_node = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed_node
    
    def print_all(self):
        if self.head is None:
            print("Empty Queue")
            return
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")


my_queue = Queue()
my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')
my_queue.enqueue('D')
my_queue.enqueue('E')
my_queue.print_all()
print("Dequeue:", my_queue.dequeue())
my_queue.print_all()






class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.tail = self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            return None
        
        removed_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed_node.data
    
    def pop_right(self):
        if self.tail is None:
            return None
        
        removed_node = self.tail
        if self.tail == self.head:
            self.tail = self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return removed_node.data
    
    def print_deque(self):
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print("None")


deque = Deque()
deque.push_left(10)
deque.push_right(20)
deque.push_left(5)
deque.push_right(25)

deque.print_deque()

print("pop_left:", deque.pop_left())
print("pop_right:", deque.pop_right())

deque.print_deque()
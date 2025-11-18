class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    # Adds Node to the end
    def append(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Adds Node to the beginning
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

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

    def print_forward(self):
        if self.head is None:
            print("Empty List")
            return
        current = self.head
        while current:
            print(current.data, end='')
            if current.next:
                print(' -> ', end='')
            current = current.next
        print()
    
    def print_backward(self):
        if self.tail is None:
            print("Empty List")
            return
        current = self.tail
        while current:
            print(current.data, end='')
            if current.prev:
                print(' <- ', end='')
            current = current.prev
        print()



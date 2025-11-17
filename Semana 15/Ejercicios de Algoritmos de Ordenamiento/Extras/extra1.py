class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def bubble_sort(self):
        if not self.head:
            return

        swapped = True
        
        while swapped:
            swapped = False
            current = self.head

            while current and current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next


ll = LinkedList()
ll.append(5)
ll.append(2)
ll.append(9)
ll.append(1)
ll.append(5)
ll.append(6)

print("Before sorting:")
ll.print_list()

ll.bubble_sort()

print("After sorting:")
ll.print_list()

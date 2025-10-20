class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        
        removed_data = self.top.data
        self.top = self.top.next
        return removed_data
    
    def print(self):
        if self.top is None:
            print("The Stack is Empty")
        else:
            current = self.top
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.print()

stack.pop()

stack.print()

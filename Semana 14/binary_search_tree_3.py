class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if not root:
            return Node(data)
        
        if data > root.data:
            root.right = self._insert(root.right, data)
        elif data < root.data:
            root.left = self._insert(root.left, data)

        return root
    
    def print_tree(self):
        self._print(self.root, 0)

    def _print(self, node, level):
        if node is not None:
            self._print(node.right, level + 1)

            print(' ' * 4 * level + '-->', node.data)

            self._print(node.left, level + 1)


if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40]

    for val in values:
        bst.insert(val)

    bst.print_tree()
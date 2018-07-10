from random import randint

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self, data=None):
        if data is None:
            self.root = None
        else:
            node = Node(data)
            self.root = node

    @staticmethod
    def print_tree(root):
        pass

    def add(self, data):
        if self.root is None:
            node = Node(data)
            self.root = node
        else:
            node = Node(data)
            if data < self.data:
                if self.left is None:
                    self.left = node
                else:
                    self.left.add(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node
                else:
                    self.right.add(data)




if __name__ == "__main__":
    tree = BinaryTree()

    for i in range(100):
        n = randint(1, 1000)
        tree.add(n)

    tree.print_tree()

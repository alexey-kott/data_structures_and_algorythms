from random import randint

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def _print_node(self, node):
        if node.left is not None:
            node._print_node(node.left)
            print(node.value)
        if node.right is not None:
            node._print_node(node.right)
            print(node.value)


class BinaryTree:
    def __init__(self, data=None):
        if data is None:
            self.root = None
        else:
            node = Node(data, 0)
            self.root = node

    def insert(self, value):
        if self.root is None:
            node = Node(value)
            self.root = node
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if node.value > value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif node.value < value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def print_tree(self):
        self.root._print_node(self.root)

    def _get_node(self):
        pass

    def get_height(self):
        node = self.root
        self.current = node




    def print_to_file(self):
        pass


if __name__ == "__main__":
    tree = BinaryTree()

    for i in range(100):
        n = randint(1, 100000)
        tree.insert(n)

    # print(tree.root.value)
    tree.print_tree()

    print(tree.get_height())

from random import randint


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.__height = None

    @property
    def height(self):  # высота поддерева с корнем в данном узле
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    def print_nodes(self, node):
        if node.left is not None:
            self.print_nodes(node.left)
            print(node.value)
        if node.right is not None:
            self.print_nodes(node.right)
            print(node.value)


class BinarySearchTree:
    def __init__(self, data=None):
        if data is None:
            self.root = None
        else:
            node = Node(data)
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
        self.root.print_nodes(self.root)

    def find_node(self, value: int):
        return self._find_node(self.root, value)

    def _find_node(self, node, value) -> Node:
        if node.value > value:
            return self._find_node(node.left, value)
        elif node.value < value:
            return self._find_node(node.right, value)

        return node

    def print_to_file(self):
        pass

    def calc_height(self):
        self._calc_height(self.root, 0)

    def _calc_height(self, node, height):
        pass


if __name__ == "__main__":
    tree = BinarySearchTree()

    for i in range(100):
        n = randint(1, 100000)
        tree.insert(n)

    tree.print_tree()

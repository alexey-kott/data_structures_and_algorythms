class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def add_value(node, value):
    if not node:
        node = TreeNode(value)
        return node

    if not value:
        return

    if node.val > value:
        if node.left:
            new_node = add_value(node.left, value)
            return new_node
        else:
            node.left = TreeNode(value)
            return node.left
    elif node.val < value:
        if node.right:
            new_node = add_value(node.right, value)
            return new_node
        else:
            node.right = TreeNode(value)
            return node.right
    else:
        print(f"Value {value} already in Tree")


def get_nodes(node):
    nodes = []
    if node.left:
        left_nodes = get_nodes(node.left)
        nodes.extend(left_nodes)

    if node.right:
        right_nodes = get_nodes(node.right)
        nodes.extend(right_nodes)

    nodes.append(node)

    return nodes


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nodes = get_nodes(root)
        values = set(map(lambda x: x.val, nodes))
        del root

        for value in values:
            n = k - value
            if n == value:
                continue

            if n in values:
                return True

        return False


def main():
    input_values = [5, 3, 6, 2, 4, None, 7]
    k = 28

    root = None

    for value in input_values:
        if not root:
            root = add_value(root, value)
        else:
            add_value(root, value)

    solution = Solution()
    result = solution.findTarget(root, k)
    print(result)


if __name__ == "__main__":
    main()

# Definition for singly-linked list.
# from itertools import zip_longest


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def zip_longest(g1, g2):
    while True:
        try:
            v1 = next(g1)
        except StopIteration:
            v1 = None
        try:
            v2 = next(g2)
        except StopIteration:
            v2 = None
        if v1 is not None or v2 is not None:
            yield v1, v2
        else:
            return


def add_node(root, value):
    if not root:
        return ListNode(value)

    node = root
    while True:
        if node.next:
            node = node.next
        else:
            new_node = ListNode(value)
            node.next = new_node
            break

    return root


def iter_list(linked_list, limit=None):
    node = linked_list
    if not limit:
        limit = get_list_length(linked_list)
    for _ in range(limit):
        value = 0 if node is None else node.val
        yield value
        if node:
            node = node.next
        if node is None and limit is None:
            return


def get_list_length(linked_list):
    counter = 0
    node = linked_list
    while True:
        if node:
            counter += 1
            node = node.next
        else:
            return counter


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        length1 = get_list_length(l1)
        length2 = get_list_length(l2)
        limit = max(length1, length2)

        g1 = iter_list(l1, limit)
        g2 = iter_list(l2, limit)
        buff = 0

        result_list = None

        for a, b in zip_longest(g1, g2):

            if a+b+buff < 10:
                result_list = add_node(result_list, a+b+buff)
                buff = 0
            else:
                n = int(str(a + b + buff)[-1])
                buff = 1
                result_list = add_node(result_list, n)

        if buff:
            result_list = add_node(result_list, buff)

        if get_list_length(result_list) == 0:
            result_list = add_node(result_list, 0)

        result = list(iter_list(result_list))
        print(result)
        return result_list

    def addTwoNumbersFast(self, l1, l2):
        n1 = int(''.join(map(lambda x: str(x), list(iter_list(l1))[::-1])))
        n2 = int(''.join(map(lambda x: str(x), list(iter_list(l2))[::-1])))
        del l1, l2

        res = list(map(lambda x: int(x), list(str(n1+n2))[::-1]))
        
        result_list = None
        for i in res:
            result_list = add_node(result_list, i)
        return result_list


if __name__ == "__main__":
    inp1 = [9, 9, 9, 9, 9, 9, 9]
    inp2 = [9, 9, 9, 9]

    inp1 = [6, 4, 5, 0, 4, 4, 9, 4, 1]
    inp2 = [3, 8, 8, 0, 3, 0, 1, 4, 8]

    root1 = None
    for item in inp1:
        root1 = add_node(root1, item)

    root2 = None
    for item in inp2:
        root2 = add_node(root2, item)

    solution = Solution()
    solution.addTwoNumbers(root1, root2)
    solution.addTwoNumbersFast(root1, root2)

# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index_map = {}
        i = 0
        next_node = head
        while True:
            if next_node:
                index_map[i] = next_node
                next_node = next_node.next if next_node.next else None
            else:
                break
            i += 1

        list_length = i
        if list_length == 1:
            return None
        if list_length - n - 1 >= 0:
            prev_node = index_map[list_length - n - 1]
            if list_length - n + 1 < list_length:
                next_node = index_map[list_length - n + 1]
            else:
                next_node = None
            prev_node.next = next_node
        else:
            next_node = index_map[list_length - n + 1]
            head = next_node

        return head


    @staticmethod
    def input_list(array: List[int]) -> Optional[ListNode]:
        prev_node: Optional[ListNode] = None
        head: Optional[ListNode] = None
        for i in array:
            node = ListNode(i)
            if not head:
                head = node
            else:
                prev_node.next = node
            prev_node = node
        return head


if __name__ == '__main__':
    list1 = [1]
    n = 1

    list_node1 = Solution.input_list(list1)

    solution = Solution()
    result_head = solution.removeNthFromEnd(list_node1, n)

    next_node = result_head
    while True:
        if next_node:
            print(next_node.val)
            next_node = next_node.next if next_node.next else None
        else:
            break

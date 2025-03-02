# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass
        if not head:
            return
        if not head.next:
            return head
        new_head = head.next
        current_node = head
        buffer_node: Optional[ListNode] = None
        while True:
            if current_node.next:
                next_pair_node = current_node.next.next
                if buffer_node:
                    buffer_node.next = current_node.next
                current_node.next.next = current_node
                current_node.next = next_pair_node
                if not next_pair_node:
                    break
                buffer_node = current_node
                current_node = next_pair_node
            else:
                break
            pass

        return new_head

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
    list1 = [1,2,3,4,5,6,7]

    list_node1 = Solution.input_list(list1)

    solution = Solution()
    result_head = solution.swapPairs(list_node1)

    next_node = result_head
    while True:
        if next_node:
            print(next_node.val)
            next_node = next_node.next if next_node.next else None
        else:
            break

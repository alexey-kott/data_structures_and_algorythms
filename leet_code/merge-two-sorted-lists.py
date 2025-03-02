# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, List


class ListNode:
    def __init__(self, val: int=0, next=None):
        self.val: int = val
        self.next: Optional['ListNode'] = next


class Solution:
    def mergeTwoLists(self, list_1: Optional[ListNode], list_2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = None
        last_node: Optional[ListNode] = None
        curr_1: Optional[ListNode] = list_1 if list_1 else None
        curr_2: Optional[ListNode] = list_2 if list_2 else None
        while True:
            if curr_1 and curr_2:
                if curr_1.val < curr_2.val:
                    current_node = curr_1
                    curr_1 = curr_1.next
                else:
                    current_node = curr_2
                    curr_2 = curr_2.next
                pass
            elif curr_1 or curr_2:
                if curr_1:
                    current_node = curr_1
                    curr_1 = curr_1.next
                elif curr_2:
                    current_node = curr_2
                    curr_2 = curr_2.next

                node = ListNode(current_node.val)
                if result_head:
                    last_node.next = node
                    last_node = node
                else:
                    last_node = node
                    result_head = last_node
                continue

            else:
                break

            node = ListNode(current_node.val)
            if result_head:
                last_node.next = node
                last_node = node
            else:
                last_node = node
                result_head = last_node

            pass

        return result_head

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
    list1 = [-9, 3]
    list2 = [5, 7]

    list_node1 = Solution.input_list(list1)
    list_node2 = Solution.input_list(list2)

    solution = Solution()
    result_head = solution.mergeTwoLists(list_node1, list_node2)

    next_node = result_head
    while True:
        if next_node:
            print(next_node.val)
            next_node = next_node.next if next_node.next else None
        else:
            break

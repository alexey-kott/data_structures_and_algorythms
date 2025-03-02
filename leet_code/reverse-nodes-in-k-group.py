from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head

        current_node = head
        while True:
            for i in range(0, k, -1):
                current_node = self.moveNode(current_node, i)



    def moveNode(self, node: ListNode, n: int) -> ListNode:
        head = None
        next_node = None
        for i in range(n):
            if next_node:
                buffer = next_node
            next_node = node.next
            next_next_node = node.next.next
            if not head:
                head = next_node
            next_node.next = node
            node.next = next_next_node
            pass

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
    list1 = [1,2,3,4,5,6]
    k = 2

    head = [1, 2, 3, 4, 5]
    k = 3

    list_node1 = Solution.input_list(list1)

    solution = Solution()
    # result_head = solution.reverseKGroup(list_node1, k)
    result_head = solution.moveNode(list_node1, 2)

    next_node = result_head
    while True:
        if next_node:
            print(next_node.val)
            next_node = next_node.next if next_node.next else None
        else:
            break

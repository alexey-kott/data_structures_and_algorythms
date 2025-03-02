package main

type ListNode struct {
	Val  int
	Next *ListNode
}

type LinkedList struct {
	head *ListNode
	tail *ListNode
}

func inputLinkedList(nums []int) LinkedList {
	var linked_list LinkedList

	for _, n := range nums {
		node := ListNode{n, nil}
		if linked_list.head == nil {
			linked_list.head = &node
			linked_list.tail = &node
		} else {
			linked_list.tail.Next = &node
			linked_list.tail = &node
		}
	}
	return linked_list
}

func deleteDuplicates(head *ListNode) *ListNode {
	var node = head
	for {
		if node.Next == nil {
			break
		}
		if node.Val == node.Next.Val {
			node.Next = node.Next.Next
		} else {
			node = node.Next
		}
	}
	return head
}

func main() {
	var arr = []int{1, 1, 2, 3, 3, 4}
	var linked_list = inputLinkedList(arr)
	deleteDuplicates(linked_list.head)
}

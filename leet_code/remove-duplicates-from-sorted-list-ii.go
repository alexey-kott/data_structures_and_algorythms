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

func getNextNode(node *ListNode) *ListNode {
	var next_node, next_node_candidate *ListNode

	for {
		if next_node_candidate == nil {
			next_node_candidate = node.Next
			if next_node_candidate.Next != nil && next_node_candidate.Val != next_node_candidate.Next.Val {
				return next_node_candidate
			}
		}

	}
}

func deleteDuplicates(head *ListNode) *ListNode {
	var node = head
	var next_node *ListNode
	for {
		if node == nil {
			break
		}
		if node.Next == nil {
			break
		}
		node = getNextNode(node)
	}

	return head
}

func main() {
	var arr = []int{1, 2, 3, 3, 3, 4, 4, 5}
	var linked_list = inputLinkedList(arr)
	deleteDuplicates(linked_list.head)
}

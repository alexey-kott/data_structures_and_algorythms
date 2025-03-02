package main

import "fmt"

func singleNumber(nums []int) int {
	var n int

	for _, value := range nums {
		n ^= value
	}
	return n
}

func main() {
	var nums = []int{4, 1, 2, 1, 2}
	// var nums = []int{2, 2, 1}
	res := singleNumber(nums)
	fmt.Println(res)
}

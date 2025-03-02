package main

import "fmt"

func twoSum(nums []int, target int) []int {
	// var diffs = make([]int, len(nums))
	var diffs = make(map[int]int)
	for index, value := range nums {
		var diff int = target - value
		diffs[diff] = index
	}

	result := []int{0, 0}
	for index, value := range nums {
		diff_index, ok := diffs[value]
		if !ok {
			continue
		}
		if index == diff_index {
			continue
		}
		result[0] = index
		result[1] = diff_index

	}

	return result
}

func main() {
	var nums = []int{2, 7, 11, 15}
	var target int = 9

	var result = twoSum(nums, target)
	fmt.Println(result)
}

package main

import "fmt"

func merge(nums1 []int, m int, nums2 []int, n int) {
	var buff_arr []int = make([]int, m+n)
	var ind1, ind2 int
	for {
		if ind1+ind2 == len(buff_arr) {
			break
		}
		if ind1 < m && ind2 < n && nums1[ind1] <= nums2[ind2] || ind2 == n {
			buff_arr[ind1+ind2] = nums1[ind1]
			ind1 += 1
		} else if ind2 < n {

			buff_arr[ind1+ind2] = nums2[ind2]
			ind2 += 1

		} else {
			break
		}

	}

	if n > 0 {

		for i, value := range buff_arr {
			nums1[i] = value
		}
	}
	return

}

func main() {
	// var nums1 = []int{1, 2, 3, 0, 0, 0}
	// m := 3
	// var nums2 = []int{2, 5, 6}
	// n := 3

	// var nums1 = []int{1}
	// m := 1
	// var nums2 = []int{}
	// n := 0

	// var nums1 = []int{1, 0}
	// m := 1
	// var nums2 = []int{2}
	// n := 1

	var nums1 = []int{2, 0}
	m := 1
	var nums2 = []int{1}
	n := 1

	merge(nums1, m, nums2, n)
	fmt.Println(nums1)
}

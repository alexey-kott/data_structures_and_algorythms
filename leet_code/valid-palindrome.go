package main

import "fmt"

func isPalindrome(str string) bool {
	var a_code = 97
	var z_code = 122
	var cap_a_code = 65
	var cap_z_code = 90
	var code_0 = 48
	var code_9 = 57
	var arr = make([]rune, 0)
	var n int
	for _, s := range str {
		n = int(s)
		if n >= cap_a_code && n <= cap_z_code {
			l := rune(n + 32)
			arr = append(arr, l)
		}
		if n >= a_code && n <= z_code {
			arr = append(arr, rune(s))
		}
		if n >= code_0 && n <= code_9 {
			arr = append(arr, rune(s))
		}
	}
	for i := 0; i < len(arr)/2; i += 1 {
		if arr[i] != arr[len(arr)-1-i] {
			return false
		}
	}
	return true
}

func main() {
	// var s = "A man, a plan, a canal: Panama"
	// var s = "0P"
	var s = " "
	result := isPalindrome(s)
	fmt.Println(result)
}

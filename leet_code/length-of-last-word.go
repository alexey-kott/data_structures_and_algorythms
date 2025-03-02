package main

import "fmt"

func lengthOfLastWord(s string) int {
	var last_length int
	var new_word bool

	for _, ch := range s {
		if ch >= 'a' && ch <= 'z' || ch >= 'A' && ch <= 'Z' {
			if new_word {
				new_word = false
				last_length = 0
			}
			last_length += 1

			continue
		}
		new_word = true

	}
	return last_length

}

func main() {
	// var input = "hello world"
	// var input = "   fly me   to   the moon  "
	// var input = "luffy is still joyboy"
	var input = "Today is a nice day"
	result := lengthOfLastWord(input)
	fmt.Println(result)
}

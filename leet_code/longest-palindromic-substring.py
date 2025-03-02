class Solution:
    def longestPalindrome(self, word: str) -> str:
        palindrome_length = 0
        palindrome_start_index = 0

        if len(word) == 1:
            return word

        if len(word) == 2:
            if word[0] == word[1]:
                return word
            return word[0]

        for i, s in enumerate(word):

            if s == 'f':
                pass

            if i == 0:
                continue
            for j in range(0, i):

                try:  # осевая симметрия
                    a = word[i-j-1]
                    b = word[i+j+1]
                except IndexError:
                    break

                if a == b:
                    length = j*2 + 3

                    if length > palindrome_length:
                        palindrome_length = length
                        palindrome_start_index = i - j
                    continue

                try:  # зеркальная
                    a = word[i-j]
                    b = word[i+j-1]
                except IndexError:
                    break

                if a == b:
                    length = j*2

                    if length > palindrome_length:
                        palindrome_length = length
                        palindrome_start_index = i - j

        return word[palindrome_start_index:palindrome_length+1]



if __name__ == "__main__":
    solution = Solution()
    # res = solution.longestPalindrome("aaaaaaddscdscsdwcwcldmks")
    # res = solution.longestPalindrome("ccd")
    # res = solution.longestPalindrome("kabcdefedcbaldkm")
    # res = solution.longestPalindrome("babad")
    res = solution.longestPalindrome("kabcdefedcbaldkm")
    # res = solution.longestPalindrome("babababab")
    print(res)
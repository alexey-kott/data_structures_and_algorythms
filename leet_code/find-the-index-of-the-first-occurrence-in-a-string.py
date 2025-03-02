from typing import Optional


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start_index = -1
        for i in range(len(haystack)):
            for j, s in enumerate(needle):
                if i+j == len(haystack):
                    return -1

                if haystack[i+j] == s:
                    if start_index == -1:
                        start_index = i
                else:
                    start_index = -1
                    break
            else:
                break

        return start_index


if __name__ == "__main__":
    haystack = "leetcode"
    needle = "ode"
    solution = Solution()
    result = solution.strStr(haystack, needle)
    print(result)

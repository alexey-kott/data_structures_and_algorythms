class Solution(object):
    def lengthOfLongestSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """

        result = []
        buffer = list()
        for i, s in enumerate(word):

            if s not in buffer:
                buffer.append(s)
            else:
                if len(buffer) > len(result):
                    result = buffer

                first_symbol_index = buffer.index(s)
                buffer = buffer[first_symbol_index+1:]
                buffer.append(s)

        if len(buffer) > len(result):
            result = buffer

        return len(result)


if __name__ == "__main__":

    solution = Solution()
    res = solution.lengthOfLongestSubstring("pwwkew")
    print(res)

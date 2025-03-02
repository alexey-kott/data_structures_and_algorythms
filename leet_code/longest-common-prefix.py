from typing import List


def get_common_prefix(word1: str, word2: str) -> str:
    prefix = ''
    short_word = min(word1, word2)
    long_word = max(word1, word2)
    for i, value in enumerate(short_word):
        if long_word[i] == value:
            prefix += value
        else:
            break
    return prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        current_symbol = None
        for i in range(len(min(strs))):
            for word in strs:
                if current_symbol == None:
                    if i < len(word):
                        current_symbol = word[i]
                    else:
                        return prefix
                else:
                    if i < len(word):
                        if current_symbol != word[i]:
                            return prefix
                    else:
                        return prefix

            else:
                prefix += current_symbol
                current_symbol = None

        return prefix

    def longestCommonPrefixOld(self, strs: List[str]) -> str:
        prefix = None

        for word in strs:
            if prefix is None:
                prefix = word
            common_prefix = get_common_prefix(word, prefix)
            if common_prefix == '':
                return common_prefix
            if common_prefix < prefix:
                prefix = common_prefix

        if prefix is not None:
            return prefix
        return ''


if __name__ == "__main__":
    solution = Solution()

    res = solution.longestCommonPrefix(["flower","flower","flower","flower"])
    print(res)

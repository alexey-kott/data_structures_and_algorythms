from functools import lru_cache
from typing import List
from itertools import permutations


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # p = set(permutations([1, -1]*n*2, n*2))

        parenthesis_str = ''.join(['()' for i in range(n)])
        perms = {''.join(item) for item in permutations(parenthesis_str, n*2)
                 if self.isValid(''.join(item))}

        return list(perms)

    @lru_cache
    def isValid(self, parenthesis: str) -> bool:
        if parenthesis[0] == ')':
            return False
        if parenthesis[-1] == '(':
            return False
        stack = []
        for s in parenthesis:
            if s == '(':
                stack.append(s)
            else:
                if len(stack) == 0:
                    return False
                stack.pop(-1)

        return True




if __name__ == "__main__":
    n = 6
    solution = Solution()
    result = solution.generateParenthesis(n)
    print(len(result))
    print(result)


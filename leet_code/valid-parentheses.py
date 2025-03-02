class Solution:
    def isValid(self, parenthesis: str) -> bool:
        stack = []
        for s in parenthesis:
            if s in ('(', '[', '{'):
                stack.append(s)
            elif s in (')', ']', '}'):
                try:
                    last_char = stack.pop(-1)
                    match last_char:
                        case '(':
                            if s != ')':
                                return False
                        case '[':
                            if s != ']':
                                return False
                        case '{':
                            if s != '}':
                                return False


                except IndexError:
                    return False
        return len(stack) == 0



if __name__ == "__main__":
    parenthesis = '{()[]{}}'
    parenthesis = '{()[]{}}}{'
    solution = Solution()
    result = solution.isValid(parenthesis)
    print(result)

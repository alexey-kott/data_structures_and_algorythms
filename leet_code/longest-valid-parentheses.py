

def get_encircle_indexes(bracket_map, start: int = 0):
    left_index = None
    right_index = None

    if start:
        i = start
        while i >= 0:
            if bracket_map[i] == 1:
                start = i
                i -= 1
            else:
                break

    for i, value in enumerate(bracket_map[start:]):
        if value == 1:
            left_index = i+start
            break
    else:
        return left_index, right_index

    for i, value in enumerate(bracket_map[left_index:]):
        if i == 0 and value != 1:
            raise ValueError
        if value == 0:
            right_index = left_index+i-1
            break
    else:
        right_index = left_index+i

    return left_index, right_index


class Solution:
    def longestValidParentheses(self, brackets: str) -> int:

        # bracket_map = [0 for _ in range(len(brackets))]
        bracket_map = bytearray(len(brackets))

        i = 0
        bracket_pairs = set()
        while i < len(brackets):
            l_bracket = brackets[i]
            if l_bracket == '(':
                try:
                    r_bracket = brackets[i+1]
                except IndexError:
                    break
                if r_bracket == ')':
                    bracket_map[i] = 1
                    bracket_map[i+1] = 1
                bracket_pairs.add((l_bracket, r_bracket))
            i += 1

        position = 0

        while True:
            left_symbol_index, right_symbol_index = get_encircle_indexes(bracket_map, position)
            if not right_symbol_index:
                break
            if left_symbol_index and right_symbol_index:
                if right_symbol_index < len(brackets)-1:
                    if brackets[left_symbol_index-1] == '(' and brackets[right_symbol_index+1] == ')':
                        flag = 1
                        bracket_map[left_symbol_index-1] = 1
                        bracket_map[right_symbol_index+1] = 1

            if right_symbol_index < len(brackets)-1:
                position = right_symbol_index+1
            else:
                break

        result = 0
        buffer = 0
        for i in bracket_map:
            if i:
                buffer += 1
                if buffer > result:
                    result = buffer
            else:
                buffer = 0

        return result


if __name__ == "__main__":
    solution = Solution()

    res = solution.longestValidParentheses('())')  #
    print(res)

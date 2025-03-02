def is_match(symb, pattern, modifier):
    if modifier == '.':
        return True

    return True


def strip_pattern(pattern: str) -> str:
    return pattern[:pattern.find('*')+1]


def is_end(string, i, pattern, j):
    if len(string) == i and len(pattern) == j:
        return True
    return False


class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        def next_symbol(string: str):
            for s in string:
                yield s
            while True:
                yield None

        get_letter = next_symbol(text)
        get_pattern = next_symbol(pattern)

        i = 0
        j = 0
        buffer = None

        while True:
            s = next(get_letter)
            p = next(get_pattern)



            if s:
                buffer = s



        while True:
            try:
                s = string[i]
                p = pattern[j]
            except IndexError:
                return False

            if s == p:
                buffer = s
                i += 1
                j += 1

            elif p == '.':
                buffer = s
                i += 1
                j += 1

            elif p == '*' and s == buffer:
                pass
                i += 1
            else:
                return False

            if is_end(string, i, pattern, j):
                return True



if __name__ == "__main__":
    solution = Solution()
    res = solution.isMatch('skmxlskmxlaksa', 'a.*dskcldks.*')  #
    print(res)

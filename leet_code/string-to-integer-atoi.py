
def check_symbol(s: str) -> bool:
    if 47 < ord(s) < 58 or ord(s) in [43, 45, 32]:  # plus, minus or space
        return True
    return False


class Solution:
    def myAtoi(self, string: str) -> int:

        string = string.strip(' +')
        for i, s in enumerate(string[::-1]):
            if s.isdigit():
                string = string[:len(string)-i]
                break

        result = ''
        parsing = 0
        for s in string:
            if parsing and not s.isdigit():
                break

            if ord(s) in [43]:  # plus
                parsing = 1
                continue
            if ord(s) in [32]:
                if parsing:
                    break
                continue
            if ord(s) == 45:
                parsing = 1
                result += s
                continue

            if s.isdigit():
                parsing = 1
                result += s
            else:
                break

        try:
            int(result)
        except ValueError:
            return 0

        n = int(result)

        if n > (2**31)-1:
            return 2**31-1
        elif n < -2**31:
            return -2**31

        return n


if __name__ == "__main__":
    solution = Solution()
    res = solution.myAtoi("   -12 32322 kdmscklm")  #
    print(res)
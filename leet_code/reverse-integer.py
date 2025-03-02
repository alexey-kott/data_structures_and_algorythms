class Solution:
    def reverse(self, x: int) -> int:


        if x < 0:
            factor = -1
            x *= -1
        else:
            factor = 1

        reversed_x = factor * int(str(x)[::-1])

        if reversed_x > (2**31)-1:
            return 0
        elif reversed_x < -2**31:
            return 0

        return reversed_x


if __name__ == "__main__":
    solution = Solution()
    res = solution.reverse(1534236469)
    print(res)
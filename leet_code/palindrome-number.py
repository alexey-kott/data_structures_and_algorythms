

class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)

        l = len(number)

        for i in range(l//2+1):
            if number[i] != number[-(i+1)]:
                return False
        return True

        for i, s in enumerate(str(number)):
            if s != number[-(i+1)]:
                return False
            if i > (l // 2) + 1:
                break
        return True



if __name__ == "__main__":
    solution = Solution()
    res = solution.isPalindrome(122343221) #
    print(res)

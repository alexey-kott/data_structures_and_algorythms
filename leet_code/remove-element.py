from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for n in nums:
            if n != val:
                i+=val

        return i


    def removeElementTrue(self, nums: List[int], val: int) -> int:
        nums_length = len(nums)
        tail_index = nums_length - 1

        i = 0
        while i <= tail_index:
            if nums[i] == val:
                nums[i] = nums[tail_index]
                del nums[tail_index]
                tail_index -= 1

            else:
                i += 1

        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    res = solution.removeElement([0,1,2,2,3,0,4,2], 2)
    print(res)

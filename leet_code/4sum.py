from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pass


if __name__ == "__main__":
    solution = Solution()
    # nums = [0, 3, 97, 102, 200]
    # target = 300
    # nums = [-4,2,2,3,3,3]
    # target = 0

    nums = [2,2,2,2,2]
    target = 8
    result = solution.fourSum(nums, target)
    print(result)

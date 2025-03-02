from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0 if target < nums[0] else 1
        if nums[-1] < target:
            return len(nums)
        if nums[0] > target:
            return 0
        if nums[0] == target:
            return 0

        left_idx = 0
        right_idx = len(nums) - 1
        while True:
            mid = right_idx - ((right_idx-left_idx) // 2)
            if nums[mid] > target:
                right_idx = mid

            elif nums[mid] < target:
                left_idx = mid
            else:
                return mid

            if right_idx - left_idx == 1:
                return right_idx



if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 2
    solution = Solution()
    result = solution.searchInsert(nums, target)
    print(result)


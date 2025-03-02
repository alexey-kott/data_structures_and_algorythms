from typing import List, Optional


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        last_num: Optional[int] = None
        num_list = []
        counter = 0
        for n in nums:
            if n != last_num:
                num_list.append(n)
                last_num = n
                counter += 1

        for i, n in enumerate(num_list):
            nums[i] = n

        for j in range(len(nums)-1, i, -1):
            del nums[j]

        return counter


if __name__ == "__main__":
    nums = [1,2,3,3,4,5, 5]
    solution = Solution()
    result = solution.removeDuplicates(nums)
    print(result)
    print(nums)



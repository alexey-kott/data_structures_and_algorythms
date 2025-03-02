from typing import List, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Tuple[int, int]:

        diffs = {}
        for i, value in enumerate(nums):
            try:
                if diffs[target-value] is not None:
                    return diffs[target-value], i
            except KeyError:
                pass
            diffs[value] = i

        a = 1



if __name__ == "__main__":
    solution = Solution()

    res = solution.twoSum([3,3], 6)  #
    print(res)
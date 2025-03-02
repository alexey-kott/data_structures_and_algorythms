from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        num_indexes = defaultdict(set)

        for n, num in enumerate(nums):
            num_indexes[num].add(n)

        for i, num_1 in enumerate(nums):
            for num_2, positions in num_indexes.items():
                if num_1 == num_2 and len(positions) == 1:
                    continue
                s = num_1 + num_2
                if s_positions := num_indexes.get(-s):
                    if -s in (num_1, num_2) and len(s_positions) in (1,2):
                        continue
                    triple = tuple(sorted([num_1, num_2, -s]))
                    result.add(triple)

        return [list(s) for s in result]



if __name__ == '__main__':
    nums = [-7, -4, -6, 6, 4, -6, -9, -10, -7, 5, 3, -1, -5, 8, -1, -2, -8, -1, 5, -3, -5, 4, 2, -5, -4, 4, 7]

    a = [[-1, -1, 2], [-9, 2, 7], [-10, 2, 8], [-5, 2, 3], [-6, -2, 8], [-8, 3, 5], [-3, -2, 5], [-8, 2, 6],
         [-4, -2, 6], [-6, -1, 7], [-5, -2, 7], [-7, -1, 8], [-10, 5, 5], [-2, -1, 3], [-7, 3, 4], [-3, -1, 4],
         [-6, 2, 4], [-5, -3, 8], [-7, 2, 5], [-10, 4, 6], [-4, -3, 7], [-9, 3, 6], [-9, 4, 5], [-4, -4, 8],
         [-4, -1, 5], [-5, -1, 6], [-10, 3, 7], [-8, 4, 4]]

    b = [[-10, 2, 8], [-10, 3, 7], [-10, 4, 6], [-10, 5, 5], [-9, 2, 7], [-9, 3, 6], [-9, 4, 5], [-8, 2, 6], [-8, 3, 5],
         [-8, 4, 4], [-7, -1, 8], [-7, 2, 5], [-7, 3, 4], [-6, -2, 8], [-6, -1, 7], [-6, 2, 4], [-5, -3, 8],
         [-5, -2, 7], [-5, -1, 6], [-5, 2, 3], [-4, -4, 8], [-4, -3, 7], [-4, -2, 6], [-4, -1, 5], [-3, -2, 5],
         [-3, -1, 4], [-2, -1, 3], [-1, -1, 2]]
    a_set = {tuple(t) for t in a}
    b_set = {tuple(t) for t in b}
    for item in b_set:
        try:
            assert item in a_set
        except AssertionError:
            pass

    nums = [-1,0,1,0]
    nums = [-1,0,1,2,-1,-4]
    result = Solution().threeSum(nums)

    print(result)

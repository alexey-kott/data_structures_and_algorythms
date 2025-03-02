from collections import defaultdict
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = None
        spread = None
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if i == j:
                    continue
                for y, k in enumerate(nums):
                    if i == y or j == y:
                        continue
                    sum = n + m + k
                    if sum == target:
                        return sum

                    if not result:
                        result = sum
                        spread = abs(target - sum)
                        continue

                    if spread > abs(target - sum):
                        result = sum
                        spread = abs(target - sum)

        return result


if __name__ == "__main__":
    solution = Solution()
    # nums = [0, 3, 97, 102, 200]
    # target = 300
    # nums = [-4,2,2,3,3,3]
    # target = 0

    nums = [173,558,-126,755,-633,899,352,-188,44,297,582,-610,690,58,-212,-775,-514,-305,-213,-905,824,674,501,-97,-158,-791,-836,428,580,-8,-545,-476,392,283,-951,778,57,-945,-736,231,-745,566,635,-955,-317,129,90,855,-989,363,648,-535,-90,-551,-593,754,-37,-857,-354,-800,391,-968,944,-343,483,-191,864,-498,-805,626,499,-981,-583,-899,-755,-41,223,-897,-10,-291,125,91,-634,-179,-703,776,775,-964,201,-640,643,609,891,612,-843,-287,620,-296,177,929,521,-306,100,984,-46,-210,794,-184,-333,-84,-206,299,-710,-931,-853,926,38,329,85,21,951,328,277,211,748,387,403,781,-890,901,692,24,405,-105,396,107,-719,-94,-396,559,93,-502,-229,-730,-283,844,34,-717,-661,662,-372,27,-284,50,-655,-492,-489,-576,55,-360,-385,-227,-249,581,484,616,-61,-35,-650,203,-473,-958,28,-638,-40,281,278,614,67,-24,394,-581,910,-297,272,-691,-81,-998,124,-761,792,355,-376,659,-509,442,-664,258,898,-673,-175,-130,921,-86,155,-497,-419,482,-468,729,-522,-269,603,444,-432,-26,-195,840,-485,-770,998,88,172,-886,-192]
    target = 7775
    result = solution.threeSumClosest(nums, target)
    print(result)

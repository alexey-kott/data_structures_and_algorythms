from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keys = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        combinations = []

        for d in digits:
            new_combinations = self.add_combinations(keys[d], combinations)
            combinations = new_combinations

        return combinations

    def add_combinations(self, key, combinations):
        result = []
        if not combinations:
            return list(key)
        for letter in key:
            for combination in combinations:
                result.append(combination+letter)

        return result




if __name__ == "__main__":
    digits = '243'
    solution = Solution()
    result = solution.letterCombinations(digits)
    print(result)


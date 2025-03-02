from typing import Tuple


class Solution(object):
    rimap = {  # Roman-to-Integer-MAP
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    irmap = {  # Integer-to-Roman-MAP
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M',
    }

    def get_roman(self, n: int, pow: int):
        order = 10**pow
        if n < 4:
            m = self.irmap[order]*n
        elif n < 5:
            m = self.irmap[order]+self.irmap[5*order]
        elif n < 9:
            m = self.irmap[5*order]+self.irmap[order]*(n-5)
        elif n < 10:
            m = self.irmap[order]+self.irmap[order*10]
        else:
            raise ValueError(n)

        return m

    def intToRoman(self, n: int) -> str:
        """
        :type n: int
        :rtype: str
        """
        result = ''

        for pow, i in enumerate(str(n)[::-1]):
            s = self.get_roman(int(i), pow)
            result = s+result

        return result

    def calc_digram(self, a: str, b: str) -> Tuple[int, int]:
        if self.rimap[a] < self.rimap[b]:
            return -1, self.rimap[b] - self.rimap[a]
        return 1, self.rimap[a]

    def romanToInt(self, s: str) -> int:

        result = 0
        i = 0
        while True:
            if i < len(s)-1:
                less, n = self.calc_digram(s[i], s[i+1])
                result += n
                if less < 0:
                    i += 2
                else:
                    i += 1
            else:
                if i != len(s):
                    result += self.rimap[s[i]]
                break

        return result


if __name__ == "__main__":
    solution = Solution()

    roman = solution.intToRoman(456)
    print(roman)
    integer = solution.romanToInt(roman)
    print(integer)

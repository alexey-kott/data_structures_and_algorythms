
def zigzag(n: int) -> [int, int]:
    x = 0
    y = 0
    while True:
        for i in range(n):
            yield x, y
            y += 1
        x += 1

        for y in range(n-2, 0, -1):
            yield x, y
            x += 1
        y = 0



class Solution:
    def convert(self, string: str, n: int) -> str:
        if n == 1:
            return string
        l = len(string)
        matrix = [[' ' for i in range(n)] for j in range(l//(n-1)+n)]

        for s, (x, y) in zip(string, zigzag(n)):
            try:
                matrix[x][y] = s
            except IndexError:
                pass

        result = ''
        for row in zip(*matrix):
            s = ''.join([s for s in row if s != ' '])
            result += s
        return result




if __name__ == "__main__":
    s = 'PAYPALISHIRING'
    s = "Ads,eetqosaaaiecwnlpnriadps,broheuefttcnedsmynhret,ieealnaioewrhanm,resecuihtbrteeaetdrintgrloalmoruornnaehwiiohaw"
    n = 4
    solution = Solution()
    result = solution.convert(s, n)
    print(result)

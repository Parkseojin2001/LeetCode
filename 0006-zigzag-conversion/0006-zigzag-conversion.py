class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        zigzag = [[] for _ in range(numRows)]

        row = 0
        flag = 0
        for char in s:
            zigzag[row].append(char)
            if row == numRows - 1:
                flag = 1
            elif row == 0:
                flag = 0

            if flag == 0:
                row += 1
            else:
                row -= 1

        result = "".join("".join(line) for line in zigzag)

        return result


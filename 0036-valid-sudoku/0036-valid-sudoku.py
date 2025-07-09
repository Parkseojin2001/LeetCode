class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(horizon):
            seen = set()
            for val in horizon:
                if val != '.' and val in seen:
                    return False
                seen.add(val)
            return True
        
        for row in board:
            if not isValid(row):
                return False
            
        for i in range(9):
            col = [row[i] for row in board]
            if not isValid(col):
                return False
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [
                    board[x][y]
                    for x in range(i, i + 3)
                    for y in range(j, j + 3)
                ]
                if not isValid(box):
                    return False
        return True
        

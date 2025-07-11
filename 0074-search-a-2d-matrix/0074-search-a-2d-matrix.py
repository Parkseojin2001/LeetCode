class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            left = 0
            right = len(m) - 1
            if m[left] <= target and m[right] >= target:
                while left <= right:
                    middle = (right + left) // 2
                    if m[middle] == target:
                        return True
                    elif m[middle] > target:
                        right = middle - 1
                    else:
                        left = middle + 1
        return False


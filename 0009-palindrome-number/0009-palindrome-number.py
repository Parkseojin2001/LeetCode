class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = str(x)
        num = list(num)
        return num[:] == num[::-1]
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^0-9a-z]', '', s)
        if s[:] == s[::-1]:
            return True
            
        else:
            return False
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        length = 0
        l, r = 0, 1
        while r < len(s):
            part = s[l:r+1]
            if len(part) == len(set(part)):
                length = max(length, len(part))
                r += 1
            else:
                l += 1
        return length



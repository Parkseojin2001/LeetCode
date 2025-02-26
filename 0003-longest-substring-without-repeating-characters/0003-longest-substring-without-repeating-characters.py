class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        start = 0
        end = 1
        length = end - start
        while end < len(s) + 1:
            if len(s[start:end]) == len(set(s[start:end])):
                if length <= len(s[start:end]):
                    length = len(s[start:end])
                    end += 1
            else:
                start += 1
                end += 1

        return length


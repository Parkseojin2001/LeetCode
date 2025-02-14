class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start_index = 0
        needle_index = 0
        i = 0
        while len(haystack) - start_index >= len(needle):
            if needle_index == len(needle):
                return start_index
            if haystack[i] == needle[needle_index]:
                i += 1
                needle_index += 1
            else:
                i = start_index + 1
                start_index = i
                needle_index = 0
        return -1


        
        return start_index
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        strs.sort()
        start = strs[0]
        last = strs[-1]
        for i in range(min(len(start), len(last))):
            if start[i] != last[i]:
                return common
            common += start[i]
        return common
            
        


            

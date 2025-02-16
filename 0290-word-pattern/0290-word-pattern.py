class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split = s.split()
        hash_p = {}
        hash_s = {}
        if len(pattern) != len(s_split):
            return False
            
        for i in range(len(pattern)):
            if pattern[i] not in hash_p:
                hash_p[pattern[i]] = i
            if s_split[i] not in hash_s:
                hash_s[s_split[i]] = i
            if hash_p[pattern[i]] != hash_s[s_split[i]]:
                return False

        return True
        
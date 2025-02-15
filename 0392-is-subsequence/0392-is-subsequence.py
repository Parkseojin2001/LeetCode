class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        t_p = 0
        s_t = 0
        for i in range(len(t)):
            if t[i] == s[s_t]:
                s_t += 1
            if s_t == len(s):
                return True
        return False
        
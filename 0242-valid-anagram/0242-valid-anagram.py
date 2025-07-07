class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_anagram = collections.Counter(s)
        t_anagram = collections.Counter(t)
        
        if t_anagram.keys() != s_anagram.keys():
            return False
        for key in s_anagram.keys():
            if s_anagram[key] != t_anagram[key]:
                return False
        return True
        
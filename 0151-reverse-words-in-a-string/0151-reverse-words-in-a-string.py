class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        words = ' '.join(words)
        return words
        
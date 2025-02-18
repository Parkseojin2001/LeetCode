class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char =='(' or char =='{' or char =='[':
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0

        
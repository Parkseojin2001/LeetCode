class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # 스택에 문자 존재 & char이 스택에 가장 마지막에 들어간 문자보다 사전 순서가 빠름 & 스택에 가장 마지막에 들어간 문자가 1개이상으로 더 남음
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return ''.join(stack)

                



        
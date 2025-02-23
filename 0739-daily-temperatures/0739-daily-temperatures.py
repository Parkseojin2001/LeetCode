class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        answer = [0 for i in range(len(t))]
        stack = []
        for i, temperature in enumerate(t):
            while stack and t[stack[-1]] < temperature:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer

            
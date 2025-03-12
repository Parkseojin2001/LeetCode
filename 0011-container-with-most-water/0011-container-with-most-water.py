class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        volume = 0
        while start < end:
            if volume < min(height[start], height[end]) * (end - start):
                volume = min(height[start], height[end]) * (end - start)
        
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return volume


        
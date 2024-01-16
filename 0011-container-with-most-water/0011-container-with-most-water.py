class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = (right - left) * min(height[left], height[right])
        for _ in range(len(height)):
            if left > right:
                break
            elif height[left] < height[right]:
                left += 1
                move_water = (right - left) * min(height[left], height[right])
                if move_water > water:
                    water = move_water
            else:
                right -= 1
                move_water = (right - left) * min(height[left], height[right])
                if move_water > water:
                    water = move_water
        return water


        
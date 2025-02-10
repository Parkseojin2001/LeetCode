class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            rest = target - n
            if rest in nums[i+1:]:
                return [i, nums[i+1:].index(rest) + i + 1]
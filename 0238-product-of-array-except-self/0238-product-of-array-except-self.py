class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        results = []
        for i in range(len(nums)):
            results.append(mul)
            mul *= nums[i]
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            results[i] *= p
            p *= nums[i]
        return results
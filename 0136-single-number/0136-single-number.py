class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()

        for i in range(0, len(nums)):
            if i == 0 and nums[i] != nums[i + 1]:
                only = nums[i]
                break
            elif i == len(nums) - 1 and nums[i] != nums[i - 1]:
                only = nums[i]
            elif nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                only = nums[i]
                break
                
        return only
        
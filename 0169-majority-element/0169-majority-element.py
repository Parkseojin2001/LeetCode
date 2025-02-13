class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        start_index = 0 
        count = 0 
        num = nums[start_index]
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if count < i - start_index:
                    num = nums[start_index]
                    count = i - start_index
                start_index = i
            elif i == len(nums) - 1:
                if count < i - start_index + 1:
                    count = i - start_index + 1
                    num = nums[i]
        return num
        
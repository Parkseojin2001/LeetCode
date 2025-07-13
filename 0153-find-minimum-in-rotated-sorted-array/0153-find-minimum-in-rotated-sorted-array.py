class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[start] < nums[mid] and nums[mid] > nums[end]:
                start = mid
            elif nums[start] <nums[mid] and nums[mid] < nums[end]:
                end = mid
            elif nums[start] > nums[mid] and nums[mid] < nums[end]:
                end = mid
            else:
                start = mid
        
        return min(nums[start], nums[end])
        
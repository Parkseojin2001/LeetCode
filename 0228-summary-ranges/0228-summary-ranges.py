class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if len(nums) == 0:
            return ranges

        first = nums[0]
        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if nums[i - 1] == first:
                    ranges.append(str(first))
                else:
                    ranges.append(f"{first}->{nums[i - 1]}")
                if i < len(nums):
                    first = nums[i]

        return ranges
            
            
        
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return nums
        ranges = []
        first = 0
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 < nums[i]:
                if nums[i - 1] == nums[first]:
                    ranges.append(f"{nums[first]}")
                else:
                    ranges.append(f"{nums[first]}->{nums[i - 1]}")
                first = i
        if first == len(nums) - 1:
            ranges.append(f"{nums[first]}")
        else:
            ranges.append(f"{nums[first]}->{nums[len(nums) - 1]}")

        return ranges

            
        return ranges
            
            
        
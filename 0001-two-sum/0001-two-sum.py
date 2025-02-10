class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        result = new_nums[left] + new_nums[right]
        while result != target:
            if result < target:
                left += 1
            elif result > target:
                right -= 1
            result = new_nums[left] + new_nums[right]
        index = []
        for i in range(len(nums)):
            if new_nums[left] == nums[i]:
                index.append(i)
            elif new_nums[right] == nums[i]:
                index.append(i)
        index = sorted(index)
        return index
        
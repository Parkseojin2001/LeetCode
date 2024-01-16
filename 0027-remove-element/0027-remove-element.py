class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
            
        while nums.count(val):
            nums.remove(val)
        print(nums)
        return len(nums)
                    
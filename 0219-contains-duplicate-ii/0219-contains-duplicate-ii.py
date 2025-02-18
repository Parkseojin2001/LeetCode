class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_n = {}

        for i, num in enumerate(nums):
            if num in hash_n and i - hash_n[num] <= k:
                return True
            else:
                hash_n[num] = i

        return False




        
        
        
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = collections.Counter(nums)

        for key in dic.keys():
            if dic[key] > 1:
                return True
        return False
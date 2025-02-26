class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        products = []

        for i in range(len(nums)):
            products.append(p)
            p = p * nums[i]
        
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= p
            p = p * nums[i]

        return products
            

        

        


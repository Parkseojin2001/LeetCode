class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        multi, num = 1, 0
        for digit in digits[::-1]:
            num = num + multi * digit
            multi *= 10
        
        num += 1
        L = list(str(num))
        
        for i in range(len(L)):
            L[i] = int(L[i])
        
        return L
        
        
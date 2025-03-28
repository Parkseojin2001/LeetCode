class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = []
        while n > 1:
            bits.append(str(n % 2))
            n = n // 2
        
        bits.append("1")
        
        count = 0
        for bit in bits:
            if bit == "1":
                count += 1
        
        return count


        
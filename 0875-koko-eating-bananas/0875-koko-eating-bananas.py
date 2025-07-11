class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        minimum_k = []

        while left <= right:
            k = (left + right) // 2
            count = 0
            for p in piles:
                count += math.ceil(p / k)
            if count > h:
                left = k + 1
            elif count < h:
                right = k - 1
                minimum_k.append(k)
            else:
                minimum_k.append(k)
                right = k - 1
                
            
        minimum_k.sort()

        return minimum_k[0]

                

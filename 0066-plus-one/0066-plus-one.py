class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        deq = collections.deque(digits)
        dum = 0
        for i in range(len(deq)-1, 0, -1):
            deq[i] += dum
            if deq[i] > 9:
                dum = 1
                deq[i] = deq[i] % 10
            else:
                dum = 0
        if dum == 1:
            deq[0] += 1
            
        if deq[0] > 9:
            deq[0] = deq[0] % 10
            deq.appendleft(1)

        return list(deq)
            
        
        
class Solution:
    def isHappy(self, n: int) -> bool:
        start_num = n
        nums = []
        while n != 1:
            str_n = str(n)
            n = 0
            for s in str_n:
                n += int(s) * int(s)
            if n in nums:
                return False
            else:
                nums.append(n)
        return True
            


        
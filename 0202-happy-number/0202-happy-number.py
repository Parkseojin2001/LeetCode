class Solution:
    def isHappy(self, n: int) -> bool:
        num_group = set()

        def get_next_number(n):
            num = 0

            while n > 0:
                digit = n % 10
                num += digit ** 2
                n = n // 10
            return num
        
        while n not in num_group:
            num_group.add(n)
            n = get_next_number(n)
            if n == 1:
                return True

        return False
        

            


        
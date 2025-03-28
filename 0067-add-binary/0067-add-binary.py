class Solution:
    def addBinary(self, a: str, b: str) -> str:

        length = min(len(a), len(b))
        index = 0
        rest = 0
        plus_ab = []

        while index < len(a) and index < len(b):
            a_num = int(a[-index - 1])
            b_num = int(b[-index - 1])
            total = a_num + b_num + rest
            if total >= 2:
                plus_ab.append(str(total % 2))
                rest = 1
            else:
                plus_ab.append(str(total))
                rest = 0
            index += 1

        i_a = index 
        i_b = index 
        while i_a < len(a):
            a_num = int(a[-i_a - 1])
            total = a_num + rest
            if total >= 2:
                plus_ab.append(str(total % 2))
                rest = 1
            else:
                plus_ab.append(str(total))
                rest = 0
            i_a += 1

        while i_b < len(b):
            b_num = int(b[-i_b-1])
            total = b_num + rest
            if total >= 2:
                plus_ab.append(str(total % 2))
                rest = 1
            else:
                plus_ab.append(str(total))
                rest = 0
            i_b += 1

        if rest == 1:
            plus_ab.append(str(rest))
        plus_ab = reversed(plus_ab)
        
        print(plus_ab)
        result = ''.join(plus_ab)
        return result
        


        
         

        
            

        
        
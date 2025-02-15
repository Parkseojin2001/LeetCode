class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dic = {}
        for i in range(len(magazine)):
            if magazine[i] not in mag_dic.keys():
                mag_dic[magazine[i]] = 1
            else:
                mag_dic[magazine[i]] += 1
        for r in ransomNote:
            if r not in mag_dic.keys():
                return False
            elif r in mag_dic.keys() and mag_dic[r] == 0:
                return False
            else:
                mag_dic[r] -= 1
        return True

        
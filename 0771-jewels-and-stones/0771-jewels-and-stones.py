class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_table = {}
        for stone in stones:
            if stone in hash_table:
                hash_table[stone] += 1
            else:
                hash_table[stone] = 1 + hash_table.get(stone, 0)
        
        count = 0
        
        for jewel in jewels:
            if jewel in hash_table:
                count += hash_table[jewel]
        return count
        
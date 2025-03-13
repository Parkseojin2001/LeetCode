class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hash_map = {}
        for i in range(0, len(citations) + 1):
            if i not in hash_map:
                hash_map[i] = 0
        
        for key in hash_map.keys():
            for citation in citations:
                if key <= citation:
                    hash_map[key] += 1
        
        h_index = 0
        for key in hash_map.keys():
            if key <= hash_map[key]:
                h_index = key
        
        return h_index


        
class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.index_map = {}
    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.lst.append(val)
        self.index_map[val] = len(self.lst) - 1
        return True
    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        index = self.index_map[val]
        self.lst[index] = self.lst[-1]
        self.index_map[self.lst[-1]] = index
        self.lst[-1] = val
        self.lst.pop()
        del self.index_map[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
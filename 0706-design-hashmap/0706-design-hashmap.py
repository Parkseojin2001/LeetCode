class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        tmp = self.table[index]
        while tmp:
            if tmp.key == key:
                tmp.value = value
                return
            if tmp.next is None:
                break
            tmp = tmp.next
        tmp.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size

        if self.table[index].value is None:
            return -1

        tmp = self.table[index]
        while tmp:
            if tmp.key == key:
                return tmp.value
            tmp = tmp.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        tmp = self.table[index]
        if tmp.key == key:
            self.table[index] = ListNode() if tmp.next is None else tmp.next
            return

        prev = tmp
        while tmp:
            if tmp.key == key:
                prev.next = tmp.next
                return
            prev, tmp = tmp, tmp.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
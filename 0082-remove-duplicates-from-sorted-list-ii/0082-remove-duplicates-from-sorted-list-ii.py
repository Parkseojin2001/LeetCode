# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_table = {}

        tmp = head

        while tmp is not None:
            if tmp.val not in hash_table:
                hash_table[tmp.val] = 1
            else:
                hash_table[tmp.val] += 1
            tmp = tmp.next
        
        new_head = ListNode()
        p = new_head

        for key in hash_table.keys():
            if hash_table[key] == 1:
                new = ListNode(key)
                p.next = new
                p = p.next
        
        return new_head.next




            
            
        
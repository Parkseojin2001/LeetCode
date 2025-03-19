# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        tmp = head
        while tmp is not None:
            length += 1
            tmp = tmp.next

        k = k % length if length != 0 else k

        if length == 0 or length == 1 or k == 0:
            return head

        start = head

        for i in range(length - k):
            prev = start
            start = start.next

        prev.next = None
        last = start

        while last.next is not None:
            last = last.next
        last.next = head
        head = start
        
        return head
        
        
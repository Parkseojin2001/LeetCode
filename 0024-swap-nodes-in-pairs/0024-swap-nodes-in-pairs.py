# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        point1, point2 = head, head.next
        while point2:
            point1.val, point2.val = point2.val, point1.val
            if point2.next == None:
                break
            point1 = point2.next
            if point1.next == None:
                break
            point2 = point1.next
        return head
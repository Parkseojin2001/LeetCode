# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None)
        tmp = head
        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = list1
                list1 = list1.next
                tmp = tmp.next

            elif list1.val > list2.val:
                tmp.next = list2
                list2 = list2.next
                tmp = tmp.next
  
            else:
                tmp.next = list1
                list1 = list1.next
                tmp = tmp.next

                tmp.next = list2
                list2 = list2.next
                tmp = tmp.next
                
            
        if list1:
            tmp.next = list1
        if list2:
            tmp.next = list2

        return head.next
        
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = head
        List = []
        while tmp != None:
            List.append(tmp.val)
            tmp = tmp.next
        left = 0
        right = len(List) - 1
        for i in range(len(List)//2):
            if List[left] != List[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

        
        
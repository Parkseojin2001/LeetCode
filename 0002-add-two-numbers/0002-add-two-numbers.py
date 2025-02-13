# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head:ListNode):
            node, prev = head, None
            while node:
                next, node.next = node.next, prev
                prev, node = node, next

            return prev
    def toList(self, node:ListNode):
            list: List = []
            while node:
                list.append(node.val)
                node = node.next
            return list
    def toReversedLinked(self, result:str):
        prev = None
        for r in result:
            node = ListNode(int(r))
            node.next = prev
            prev = node
        return node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverse(l1))
        b = self.toList(self.reverse(l2))

        result = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

        return self.toReversedLinked(str(result))
        
        
            
            
        
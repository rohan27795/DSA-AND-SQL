# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode()
        current = dummy
        carry=0
        while l1 or l2 or carry:
            val1= l1.val if l1 else 0
            val2= l2.val if l2 else 0

            val = val1 + val2+ carry
            carry = val // 10
            new_val = val % 10

            current.next = ListNode(new_val)

            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
        
        




        
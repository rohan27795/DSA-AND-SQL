# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        prev=slow.next=None
        while second:
            nxt = second.next
            second.next=prev
            prev=second
            second=nxt
        first,second=head,prev
        while second:
            temp1,temp2=first.next,second.next
            first.next=second
            second.next=temp1
            first,second=temp1,temp2
            

        
        
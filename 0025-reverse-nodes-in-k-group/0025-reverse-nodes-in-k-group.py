# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0,head)
        groupprev = dummy
        while True:
            kth = self.getkth(groupprev,k)
            if not kth:
                break
            groupnext = kth.next
            prev,curr = kth.next,groupprev.next
            while curr != groupnext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            tmp = groupprev.next
            groupprev.next = kth
            groupprev = tmp

        return dummy.next

    def getkth(self,curr,k):
        while curr and k > 0:
            curr = curr.next
            k-=1
        return curr
    

        
        
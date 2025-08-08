class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minheap = []
        for num in nums:
            if len(minheap) < k:
                heapq.heappush(minheap,num)

            else:
                heapq.heappushpop(minheap,num)
                    
        return minheap[0]

            

    


        
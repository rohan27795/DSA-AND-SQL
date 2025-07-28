class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)  # O(n)
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for (freq, num) in min_heap]

            
        
    
    






        
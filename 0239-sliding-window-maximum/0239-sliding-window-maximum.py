class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        i = 0
        j = 0 
        n = len(nums)
        ans = []
        d = deque()
        while j < n:
            while d and d[-1]<nums[j]:
                d.pop()
            d.append(nums[j])

            if j-i+1 < k:
                j +=1

            elif j-i+1 == k:
                ans.append(d[0])
                if d[0] == nums[i]:
                    d.popleft()
                i +=1
                j +=1
        
        return ans
        
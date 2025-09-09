class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m == 0:
            return 0
        if m == 1:
            return nums[0]
        
        return max(self.rob_linear(nums[1:]),self.rob_linear(nums[:-1]))
        
            

    def rob_linear(self,nums):
        n = len(nums)

        if n == 0:
            return 0

        if n == 1:
            return nums[0]
        
        t = [0] * n

        t[0] = nums[0]
        t[1] = max(nums[0],nums[1])

        for i in range(2,n):
            t[i] = max(nums[i] + t[i-2] , t[i-1])

        return t[-1]
        

        
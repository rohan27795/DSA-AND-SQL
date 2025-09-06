class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        totalsum = sum(nums)
    
    # If sum is odd, cannot partition into 2 equal subsets
        if totalsum % 2 != 0:
            return False

    # Check if subset with sum = totalsum/2 exists
        return self.subsetsum(nums, totalsum // 2)

    def subsetsum(self,nums, sums):
        n = len(nums)
        t = [[False] * (sums + 1) for _ in range(n + 1)]

    # Base case: sum = 0 is always possible
        for i in range(n + 1):
            t[i][0] = True

    # Fill DP table
        for i in range(1, n + 1):
            for j in range(1, sums + 1):
                if nums[i - 1] <= j:
                    t[i][j] = t[i - 1][j - nums[i - 1]] or t[i - 1][j]
                else:
                    t[i][j] = t[i - 1][j]

        return t[n][sums]


        

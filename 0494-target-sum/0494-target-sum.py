class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total = sum(nums)

        # Not possible case
        if total < abs(target) or (total + target) % 2 != 0:

            return 0

        subset_sum = (total + target) // 2

        # Count subsets with sum = subset_sum
        return self.countSubsets(nums, subset_sum)

    def countSubsets(self, nums, target_sum):
        n = len(nums)
        t = [[0] * (target_sum + 1) for _ in range(n + 1)]

        # Base case: 1 way to make sum=0 (pick nothing)
        for i in range(n + 1):
            t[i][0] = 1

        for i in range(1, n + 1):
            for j in range(target_sum + 1):
                if nums[i - 1] <= j:
                    t[i][j] = t[i - 1][j] + t[i - 1][j - nums[i - 1]]
                else:
                    t[i][j] = t[i - 1][j]

        return t[n][target_sum]


    


        

        
            
            

        
        
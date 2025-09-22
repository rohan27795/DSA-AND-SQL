class Solution(object):
    def subsets(self, nums):
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])  # copy current subset
                return 
        
        # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

        # Backtrack (remove nums[i])
            subset.pop()

        # Exclude nums[i]
            dfs(i + 1)

        dfs(0)
        return res

        

        
        






        
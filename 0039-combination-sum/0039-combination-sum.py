class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        subset = []
        def dfs(i,total):
            if total == target:
                res.append(subset[:])
                return
            
            if i >=len(candidates) or total > target:
                return 
                
            subset.append(candidates[i])
            dfs(i,total + candidates[i])

            subset.pop()
            dfs(i+1,total)

        dfs(0,0)
        return res
                
            
        
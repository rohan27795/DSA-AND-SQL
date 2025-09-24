class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        subset = []
        def dfs(i,total):
            if total == target:
                res.append(subset[:])
                return
            
            if i >= len(candidates) or total > target:
                return 
                
            subset.append(candidates[i])
            dfs(i+1,total + candidates[i]) #multiple value

            subset.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i +=1
            dfs(i+1,total)   #exclude

        dfs(0,0)
        return res


        

                

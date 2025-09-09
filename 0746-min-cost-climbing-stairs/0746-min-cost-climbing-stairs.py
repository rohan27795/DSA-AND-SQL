class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        t = [0] * (n+1)

        t[0] = 0
        t[1] = 0

        for i in range(2,n+1):
            
            t[i] = min(t[i-1]+cost[i-1],t[i-2]+cost[i-2])

        return t[n]
        
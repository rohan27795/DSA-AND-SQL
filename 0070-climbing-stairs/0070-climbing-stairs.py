class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = [0] *(n +1)

        t[0] = 1  #one way to reach 0 step
        t[1] = 1  #one way to reach 1st step
        
        for i in range(2,n+1):
            t[i] = t[i-1] + t[i-2] # no of ways to reach a particular step is sum of
                                     #ways to reach previous two step
            

        return t[n]
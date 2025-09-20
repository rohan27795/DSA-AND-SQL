class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        m = n 
        ans = 1.0
        n = abs(n)
        while n > 0:
            if n % 2 == 1:
                ans *= x
                n -= 1
            else:
                x *= x
                n //= 2
            
        if m < 0:
            ans = 1.0 / ans
        return ans







                
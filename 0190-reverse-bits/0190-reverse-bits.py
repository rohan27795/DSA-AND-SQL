class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(32):
            b = (n>>i) & 1

            ans = ans|(b <<(31-i))
            
        return ans
        
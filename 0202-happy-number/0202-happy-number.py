class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.SumOfSquare(n)
            if n == 1:
                return True
                            

        return False

    def SumOfSquare(self,n):
        output = 0
        
        while n:

            lastdigit = n % 10
            output += lastdigit * lastdigit
            n = n // 10
        return output
        



        
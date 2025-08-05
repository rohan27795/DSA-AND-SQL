class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = []
        for i,currenttemperature in enumerate(temperatures):
            while stack and currenttemperature > stack[-1][0]:
                stacktemp,stackindex = stack.pop()
                res[stackindex] = (i-stackindex)
            stack.append([currenttemperature,i])
         
        return res
        
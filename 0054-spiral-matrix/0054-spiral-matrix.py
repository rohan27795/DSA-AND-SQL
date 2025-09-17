class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        l = 0
        r = len(matrix[0])
        top = 0
        bottom = len(matrix)
        
        while l<r and top<bottom:
            for i in range(l,r):
                ans.append(matrix[top][i])
            top +=1

            for i in range(top,bottom):
                ans.append(matrix[i][r-1])
            r -=1

            if not (l < r and top < bottom):
                break


            for i in range(r-1,l-1,-1):
                ans.append(matrix[bottom-1][i])
            bottom -=1

            for i in range(bottom-1,top-1,-1):
                ans.append(matrix[i][l])
            l +=1

        return ans
            


        
        
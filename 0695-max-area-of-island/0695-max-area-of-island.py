class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row,col = len(grid) , len(grid[0])
        visit = set()
        def dfs(i,j):
            if i<0 or i>=row or j<0 or j>=col or (i,j) in visit or grid[i][j] == 0:
                return 0
            
            visit.add((i,j))
            return(1+dfs(i+1,j)+
                     dfs(i-1,j)+
                     dfs(i,j+1)+
                     dfs(i,j-1))

        area = 0
        for i in range(row):
            for j in range(col):
                area = max(area, dfs(i,j))

        return area

    
                



        
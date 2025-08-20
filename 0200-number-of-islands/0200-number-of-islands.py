class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row,col = len(grid) , len(grid[0])
        num_island = 0

        def dfs(i,j):
            if i<0 or i>=row or j<0 or j>=col or grid[i][j] !='1':
                return 
            else:
                grid[i][j] = '0'
                dfs(i,j+1)
                dfs(i,j-1)
                dfs(i-1,j)
                dfs(i+1,j)


        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    num_island +=1
                    dfs(i,j)
        
        return num_island
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        time = 0
        fresh = 0
        row,col = len(grid),len(grid[0])
         
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append([r,c])

        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    nr,nc = r + dr, c + dc

                    if (nr<0 or nr>=row or nc<0 or 
                       nc>=col or grid[nr][nc] !=1):
                       continue

                    grid[nr][nc] = 2
                    q.append([nr,nc])
                    fresh -=1

            time +=1

        return time if fresh == 0 else -1
            

            


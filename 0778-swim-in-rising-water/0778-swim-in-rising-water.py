class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        minheap = [[grid[0][0],0,0]]
        visit = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        #visit.add((0,0))
        while minheap:
            time,r,c = heapq.heappop(minheap)
            if r == N-1 and c == N-1:
                return time
            for dr,dc in directions:
                nei_r,nei_c = r+dr,c+dc
                if (nei_r<0 or nei_c<0 or nei_r>=N or nei_c>=N
                    or (nei_r,nei_c) in visit):
                    continue
                visit.add((nei_r,nei_c))
                heapq.heappush(minheap,[max(time,grid[nei_r][nei_c]),nei_r,nei_c])


    



    

                                                  

                                   



        
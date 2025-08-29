class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N = len(points)
        adj = {i:[] for i in range(N)}
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                distance = abs(x1-x2)+abs(y1-y2)
                adj[i].append([distance,j])
                adj[j].append([distance,i])


        res = 0
        minheap = [[0,0]]
        visit = set()
        while len(visit)<N:
            cost,i = heapq.heappop(minheap)
            if i in visit:
                continue
            res += cost
            visit.add(i)

            for neighbourcost,neighbour in adj[i]:
                if neighbour not in visit:
                    heapq.heappush(minheap,[neighbourcost,neighbour])

        return res











        
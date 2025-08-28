class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        edges = collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))

        minheap = [(0,k)]
        visit = set()
        time = 0

        while minheap:
            w1,n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            time = max(time,w1)

            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap,(w1+w2,n2))

        return time if len(visit) == n else -1

        


        
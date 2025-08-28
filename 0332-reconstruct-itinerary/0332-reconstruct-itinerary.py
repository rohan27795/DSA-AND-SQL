class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        import heapq

    # adjacency list with min-heap for lexicographic order
        adj = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)

        res = []

        def dfs(src):
            while adj[src]:
                dfs(heapq.heappop(adj[src]))
            res.append(src)

        dfs("JFK")
        return res[::-1]  # reverse to get correct path

        


            



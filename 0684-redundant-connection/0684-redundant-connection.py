class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = len(edges)
        parent = [i for i in range(N+1)]
        rank = [1] * (N+1)

        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])
            return parent[n]

        def union(n1,n2):
            parent1,parent2 = find(n1),find(n2)
             
            if parent1 == parent2:
                return False

            if rank[parent1]<rank[parent2]:
                parent[parent1] = parent2
            elif rank[parent2]<rank[parent1]:
                parent[parent2] = parent2
            else:
                parent[parent1] = parent2
                rank[parent1] = rank[parent1] +1
            return True

        for n1,n2 in edges:
            if not union(n1,n2):
                return[n1,n2]



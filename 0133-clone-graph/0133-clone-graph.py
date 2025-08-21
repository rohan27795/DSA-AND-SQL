"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        oldtonew = {}

        def dfs(node):
            if not node:
                return None

        
            if node in oldtonew:
                return oldtonew[node]

            copy = Node(node.val)
            oldtonew[node] = copy

            for nie in node.neighbors:
                copy.neighbors.append(dfs(nie))
            return copy

        return dfs(node) 


            

        
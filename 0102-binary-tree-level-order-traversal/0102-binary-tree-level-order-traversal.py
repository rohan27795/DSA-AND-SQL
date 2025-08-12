# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res = []
        q = collection.deque()
        q.append(root)
        
        while q:
            lenq = len(q)
            level = []
            for i in range lenq:
                node = q,popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

                res.append(leval)
        return res

        
    
            


        
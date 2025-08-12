# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right
class Solution(object):
    def inorderTraversal(self,root):
        res =[]
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res



            
        
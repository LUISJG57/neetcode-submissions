# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, maximo):
            nonlocal res
            if not node:
                return
            if node.val >= maximo:
                res+=1
            maximo = max(maximo, node.val)
            dfs(node.left, maximo)
            dfs(node.right, maximo)
        dfs(root, root.val)
        return res
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copy = {}
        def dfs(node):
            if node in copy:
                return copy[node]
            dup = Node(node.val)
            copy[node] = dup
            for nei in node.neighbors:
                dup.neighbors.append(dfs(nei))
            return dup
        return dfs(node) if node else None
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def dfs(node):
            if not node:
                return None
            if node.val == p or node.val == q:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            return left or right

        def dist(node, target, d):
            if not node:
                return -1
            if node.val == target:
                return d
            left = dist(node.left, target, d + 1)
            right = dist(node.right, target, d + 1)
            return max(left, right)

        lca = dfs(root)
        return dist(lca, p, 0) + dist(lca, q, 0)
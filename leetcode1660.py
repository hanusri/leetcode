from typing import N
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        visited = set()

        def dfs(node):
            if not node:
                return None
            if node.right and node.right.val in visited:
                return None
            visited.add(node.val)
            node.right = dfs(node.right)
            node.left = dfs(node.left)
            return node
        
        return dfs(root)
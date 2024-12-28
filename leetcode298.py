from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.max_length = 1
        def dfs(root: Optional[TreeNode], length: int):
            if root is None:
                return
            
            if root.left and root.left.val - root.val == 1:
                self.max_length = max(self.max_length, length + 1)
                dfs(root.left, length + 1)
            else:
                dfs(root.left, 1)
            
            if root.right and root.right.val - root.val == 1:
                self.max_length = max(self.max_length, length + 1)
                dfs(root.right, length + 1)
            else:
                dfs(root.right, 1)

            return
        
        dfs(root, 1)
        return self.max_length
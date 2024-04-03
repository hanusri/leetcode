from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = float('inf')

        def inOrder(node):
            nonlocal k, res
            if not node:
                return
            inOrder(node.left)
            k -= 1
            if k == 0:
                res = node.val
                return
            inOrder(node.right)
        
        inOrder(root)
        return res
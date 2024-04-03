from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minVal = float('inf')
        prev = None

        def inOrder(node):
            nonlocal minVal, prev
            if not node:
                return
            inOrder(node.left)
            if prev:
                minVal = min(minVal, node.val - prev.val)
            prev = node
            inOrder(node.right)
        
        inOrder(root)
        return minVal
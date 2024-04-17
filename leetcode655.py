from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self.get_height(root)
        width = (1 << height) - 1
        res = [[''] * width for _ in range(height)]
        
        def fill(node, level, left, right):
            if not node:
                return
            mid = (left + right) >> 1
            res[level][mid] = str(node.val)
            fill(node.left, level + 1, left, mid - 1)
            fill(node.right, level + 1, mid + 1, right)
        
        fill(root, 0, 0, width - 1)
        return res
        
    def get_height(self, node):
        return 0 if not node else 1 + max(self.get_height(node.left), self.get_height(node.right))
        return res
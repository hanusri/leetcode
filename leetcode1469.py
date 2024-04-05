from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node,par):
            if node:
                if par and (not par.left)^(not par.right): res.append(node.val) 
                dfs(node.left,node)
                dfs(node.right,node)
                return res 
        return dfs(root,None)
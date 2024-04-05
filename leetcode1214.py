from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def dfs(node, nodeset):
            if node:
                nodeset.add(node.val)
                dfs(node.left, nodeset)
                dfs(node.right, nodeset)

        def find(node, nodeset):
            if node:
                if target - node.val in nodeset:
                    return True
                return find(node.left, nodeset) or find(node.right, nodeset)
            return False

        nodeset = set()
        dfs(root1, nodeset)
        return find(root2, nodeset)
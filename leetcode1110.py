from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        res = []

        def dfs(node, is_isolated):
            if not node:
                return None
            to_delete = node.val in to_delete_set
            if not to_delete and is_isolated:
                res.append(node)
            node.left = dfs(node.left, to_delete)
            node.right = dfs(node.right, to_delete)
            return None if to_delete else node

        dfs(root, True)
        return res
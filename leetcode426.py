from typing import Optional
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None
        first = None
        last = None
        def dfs(node):
            nonlocal first
            nonlocal last
            if not node:
                return
            dfs(node.left)
            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node
            dfs(node.right)
        dfs(root)
        last.right = first
        first.left = last
        return first
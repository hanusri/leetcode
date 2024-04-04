from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0
        self.dfs(root, distance)
        return self.count
    
    def dfs(self, node: TreeNode, distance: int) -> List[int]:
        if node is None:
            return []
        if node.left is None and node.right is None:
            return [0]
        left = self.dfs(node.left, distance)
        right = self.dfs(node.right, distance)
        for l in left:
            for r in right:
                if l + r + 2 <= distance:
                    self.count += 1
        return [n + 1 for n in left + right if n + 1 < distance]
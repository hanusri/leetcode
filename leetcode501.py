from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = 0
        max_count = 0
        prev = None
        modes = []
        def inorder(node):
            nonlocal count, max_count, prev, modes
            if not node:
                return
            inorder(node.left)
            if prev == node.val:
                count += 1
            else:
                count = 1
            if count == max_count:
                modes.append(node.val)
            elif count > max_count:
                modes = [node.val]
                max_count = count
            prev = node.val
            inorder(node.right)
        inorder(root)
        return modes
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return root.val == 1
        leftValue = self.evaluateTree(root.left)
        rightValue = self.evaluateTree(root.right)

        ans = False

        if root.val == 2:
            ans = leftValue or rightValue
        elif root.val == 3:
            ans = leftValue and rightValue

        return ans